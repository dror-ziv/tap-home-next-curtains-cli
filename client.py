from protobuf_decoder.protobuf_decoder import Parser, ParsedResults
import asyncio
import websockets
import binascii

from protobuf_objects import (
    hex_with_spaces,
    login_command,
    devices,
    device_id,
    taphome_set_curtain_command,
)
from settings import (
    TapHomeClientSettings,
    Curtain,
    CurtainLevel,
    load_my_curtains_from_cache,
    set_my_curtains_cache,
)


def _commands(level: CurtainLevel, curtains: list[Curtain]) -> list[str]:
    return [taphome_set_curtain_command(curtain, level) for curtain in curtains]


def _filter_target_curtains(
    payload: ParsedResults, curtains_names: list[str]
) -> list[Curtain]:
    payload_devices = devices(payload)
    return [
        Curtain(name=name, id=device_id(name, payload_devices))
        for name in curtains_names
    ]


async def _send_hex_message(ws, message):
    await ws.send(binascii.unhexlify(message.replace(" ", "")))


async def _wait_for_response(ws):
    return await ws.recv()


async def _send_commands(ws, commands: list[str]):
    for command in commands:
        await _send_hex_message(ws, command)
        await _wait_for_response(
            ws,
        )
        print(f"set curtain command was sent")


async def _connect_and_setup(settings: TapHomeClientSettings) -> list[Curtain]:
    async with websockets.connect(settings.server_url) as ws:
        print("WebSocket connection established!")
        await _send_hex_message(
            ws,
            hex_with_spaces(login_command(settings.username, settings.hashed_password)),
        )
        response = await _wait_for_response(ws)
        print("Logged-in Successfully")
        print("parsing response...")
        parsed_response = Parser().parse(hex_with_spaces(response))
        my_curtains = _filter_target_curtains(
            parsed_response, settings.my_curtains_names
        )
        set_my_curtains_cache(my_curtains)
        print("Setup Completed Successfully")
        return my_curtains


async def _connect_and_send_commands(
    level: CurtainLevel, settings: TapHomeClientSettings, curtains: list[Curtain]
):
    async with websockets.connect(settings.server_url) as ws:
        print("WebSocket connection established!")
        await _send_hex_message(
            ws,
            hex_with_spaces(login_command(settings.username, settings.hashed_password)),
        )
        response = await _wait_for_response(ws)
        print("Logged-in successfully")
        await asyncio.sleep(1)
        await _send_commands(ws, _commands(level, curtains))


def _raise_invalid_arguments_error():
    raise ValueError("Error: Invalid arguments. Usage: python main.py [up/down/setup]")


def _validate_cache(my_curtains_names: list[str]):
    cached_curtains_names = [curtain.name for curtain in load_my_curtains_from_cache()]
    for curtain in my_curtains_names:
        if curtain not in cached_curtains_names:
            raise ValueError(
                "Error: cache does not match config file. Please Run setup."
            )


def set_curtains(
    curtains: list[str], settings: TapHomeClientSettings, level: CurtainLevel
):
    settings.my_curtains_names = curtains
    curtains = asyncio.get_event_loop().run_until_complete(_connect_and_setup(settings))
    asyncio.get_event_loop().run_until_complete(
        _connect_and_send_commands(settings=settings, level=level, curtains=curtains)
    )
