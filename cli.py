import asyncio
import sys

from client import (
    _raise_invalid_arguments_error,
    _connect_and_setup,
    _validate_cache,
    _connect_and_send_commands,
)
from settings import load_from_config, CurtainLevel, load_my_curtains_from_cache, set_my_curtains_cache


def main():
    settings = load_from_config()
    if len(sys.argv) != 2:
        _raise_invalid_arguments_error()
    arg = sys.argv[1].lower()

    if arg == "setup":
        curtains = asyncio.get_event_loop().run_until_complete(_connect_and_setup(settings))
        set_my_curtains_cache(curtains)
        return

    if arg == "up":
        level = CurtainLevel.UP
    elif arg == "down":
        level = CurtainLevel.DOWN
    else:
        _raise_invalid_arguments_error()
        return  # for lint purposes
    _validate_cache(settings.my_curtains_names)
    asyncio.get_event_loop().run_until_complete(
        _connect_and_send_commands(
            settings=settings, level=level, curtains=load_my_curtains_from_cache()
        )
    )


if __name__ == "__main__":
    main()
