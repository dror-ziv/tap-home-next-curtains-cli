from client import set_curtains
from models import (
    SetCurtainsDownCommand,
    SetCurtainsUpCommand,
    DOWN_COMMAND,
    UP_COMMAND,
)
from settings import CurtainLevel, TapHomeClientSettings

_SETTINGS = TapHomeClientSettings()


def handle_event(event, context):
    if event["type"] == DOWN_COMMAND:
        command = SetCurtainsDownCommand.model_validate(event)
        set_curtains(command.data.curtain_ids, _SETTINGS, CurtainLevel.DOWN)
    elif event["type"] == UP_COMMAND:
        command = SetCurtainsUpCommand.model_validate(event)
        set_curtains(command.data.curtain_ids, _SETTINGS, CurtainLevel.UP)
    else:
        raise ValueError(f"Invalid Command {event}")
