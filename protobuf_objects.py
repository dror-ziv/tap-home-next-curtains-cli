from typing import Union

from protobuf_decoder.protobuf_decoder import Parser, ParsedResults, FixedBitsValue

import protobuf_structure_pb2
from settings import Curtain, CurtainLevel


def _set_curtain_command(curtain: Curtain, level: CurtainLevel):
    new_object = protobuf_structure_pb2.SetDeviceCommand()
    new_curtain = new_object.field101
    new_curtain.maybeCurtainId = curtain.id
    new_curtain.deviceName = curtain.name
    new_curtain.attributeName = "slide-level"
    if level == CurtainLevel.UP:
        new_curtain.field4.field103.Field1 = 0  # we must set this field to 0 for the server to validate the protobuf struct # noqa
    elif level == CurtainLevel.DOWN:
        new_curtain.field4.field103.Field1 = 4607182418800017408  # we must set this magic number when setting the curtain level to 0 # noqa
    new_object.setLevelTo = level.value
    return new_object


def hex_with_spaces(str_hex):
    return str(' '.join([format(byte, '02x') for byte in str_hex]))


def _adapt_set_curtain_command_to_taphome(command: str) -> str:
    id_part, command = command[:2], command[2:]
    new_command = command + id_part
    return new_command


def taphome_set_curtain_command(curtain: Curtain, level: CurtainLevel) -> str:
    return hex_with_spaces(_adapt_set_curtain_command_to_taphome(_set_curtain_command(curtain, level).SerializeToString(deterministic=True)))


def login_command(username: str, hashed_password: str) -> str:
    new_object = protobuf_structure_pb2.LoginCommand()
    login_object = new_object.field108
    inner_login = login_object.field1
    inner_login.field1 = 5247652847443983827  # magic number
    inner_login.field2 = 7015745339595105168  # magic number
    login_object.Email = username
    login_object.HashedPassword = hashed_password
    login_object.Platform = "Android"
    login_object.AppVersion = "2023.2.28594"
    login_object.DeviceId = "4adc2bb1da60c180"  # the device id of the original genymobile emulated device
    login_object.DeviceInformation = "Genymobile Nexus 5, Android 11"
    login_object.field10 = 77  # magic number
    return new_object.SerializeToString(deterministic=True)


def _first_field(protobuf_obj: ParsedResults, target_field: int) -> Union[str, int, FixedBitsValue, ParsedResults]:
    for i in protobuf_obj.results:
        if i.field == target_field:
            return i.data
    raise ValueError("no field found")


def _fields(protobuf_obj: ParsedResults, target_field: int) -> list[ParsedResults]:
    result = []
    for i in protobuf_obj.results:
        if i.field == target_field:
            result.append(i.data)
    if result:
        return result
    raise ValueError("no field found")


def object_by_field(objects: list[ParsedResults], target_value: str, field: int) -> ParsedResults:
    for obj in objects:
        if _first_field(obj, field) == target_value:
            return obj
    raise ValueError("no field found")


def devices(payload: ParsedResults) -> list[ParsedResults]:
    return _fields(_first_field(payload, 109), 7)  # magic field numbers.


DEVICE_NAME_FIELD = 2
DEVICE_ID_FIELD = 1

def device_id(name: str, my_devices: list[ParsedResults]) -> int:
    my_device = object_by_field(my_devices, name, DEVICE_NAME_FIELD)
    return _first_field(my_device, 1)


