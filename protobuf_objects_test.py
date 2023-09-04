from protobuf_objects import CurtainLevel, taphome_set_curtain_command

from settings import Curtain


UP_14 = "aa 06 1b 08 60 12 05 49 31 34 40 40 1a 0b 73 6c 69 64 65 2d 6c 65 76 65 6c 22 03 ba 06 00 08 5c"
DOWN_14 = "aa 06 24 08 60 12 05 49 31 34 40 40 1a 0b 73 6c 69 64 65 2d 6c 65 76 65 6c 22 0c ba 06 09 09 00 00 00 00 00 00 f0 3f 08 06"

UP_15 = "aa 06 1c 08 ec 01 12 05 49 31 35 40 40 1a 0b 73 6c 69 64 65 2d 6c 65 76 65 6c 22 03 ba 06 00 08 5c"
DOWN_15 = "aa 06 25 08 ec 01 12 05 49 31 35 40 40 1a 0b 73 6c 69 64 65 2d 6c 65 76 65 6c 22 0c ba 06 09 09 00 00 00 00 00 00 f0 3f 08 5c"

DOWN_16 = "aa 06 24 08 ed 01 12 04 49 31 36 40 1a 0b 73 6c 69 64 65 2d 6c 65 76 65 6c 22 0c ba 06 09 09 00 00 00 00 00 00 f0 3f 08 06"
UP_16 = "aa 06 1b 08 ed 01 12 04 49 31 36 40 1a 0b 73 6c 69 64 65 2d 6c 65 76 65 6c 22 03 ba 06 00 08 5c"


def test_create_set_curtain_level_up():
    command = taphome_set_curtain_command(Curtain(name="I14@@", id=96), CurtainLevel.UP)
    assert command == UP_14


def test_create_set_curtain_level_down():
    command = taphome_set_curtain_command(Curtain(name="I14@@", id=96), CurtainLevel.DOWN)
    assert command == DOWN_14


