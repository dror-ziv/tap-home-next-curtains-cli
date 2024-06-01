from pydantic import BaseModel


class CurtainsLevelToBeChanged(BaseModel):
    curtain_ids: list[str]

    class Config:
        extra = "ignore"


UP_COMMAND = "com.taphome.curtains.SetCurtainsUpCommand"


class SetCurtainsUpCommand(BaseModel):
    type: str = UP_COMMAND
    data: CurtainsLevelToBeChanged

    class Config:
        extra = "ignore"


DOWN_COMMAND = "com.taphome.curtains.SetCurtainsDownCommand"


class SetCurtainsDownCommand(BaseModel):
    type: str = DOWN_COMMAND
    data: CurtainsLevelToBeChanged

    class Config:
        extra = "ignore"
