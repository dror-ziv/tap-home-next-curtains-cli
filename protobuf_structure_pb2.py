# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf_structure.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18protobuf_structure.proto\"$\n\x12NestedNestedDevice\x12\x0e\n\x06\x46ield1\x18\x01 \x01(\x06\"5\n\x0cNestedDevice\x12%\n\x08\x66ield103\x18g \x01(\x0b\x32\x13.NestedNestedDevice\"j\n\x06\x44\x65vice\x12\x16\n\x0emaybeCurtainId\x18\x01 \x01(\x05\x12\x12\n\ndeviceName\x18\x02 \x01(\t\x12\x15\n\rattributeName\x18\x03 \x01(\t\x12\x1d\n\x06\x66ield4\x18\x04 \x01(\x0b\x32\r.NestedDevice\"A\n\x10SetDeviceCommand\x12\x12\n\nsetLevelTo\x18\x01 \x01(\x05\x12\x19\n\x08\x66ield101\x18\x65 \x01(\x0b\x32\x07.Device\"\xd0\x02\n\x0cLoginCommand\x12\x31\n\x08\x66ield108\x18l \x01(\x0b\x32\x1f.LoginCommand.InnerLoginCommand\x1a\x8c\x02\n\x11InnerLoginCommand\x12<\n\x06\x66ield1\x18\x01 \x01(\x0b\x32,.LoginCommand.InnerLoginCommand.UnknownInner\x12\r\n\x05\x45mail\x18\x02 \x01(\t\x12\x16\n\x0eHashedPassword\x18\x03 \x01(\t\x12\x10\n\x08Platform\x18\x04 \x01(\t\x12\x12\n\nAppVersion\x18\x05 \x01(\t\x12\x10\n\x08\x44\x65viceId\x18\x06 \x01(\t\x12\x19\n\x11\x44\x65viceInformation\x18\x07 \x01(\t\x12\x0f\n\x07\x66ield10\x18\n \x01(\x05\x1a.\n\x0cUnknownInner\x12\x0e\n\x06\x66ield1\x18\x01 \x01(\x06\x12\x0e\n\x06\x66ield2\x18\x02 \x01(\x06\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protobuf_structure_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_NESTEDNESTEDDEVICE']._serialized_start=28
  _globals['_NESTEDNESTEDDEVICE']._serialized_end=64
  _globals['_NESTEDDEVICE']._serialized_start=66
  _globals['_NESTEDDEVICE']._serialized_end=119
  _globals['_DEVICE']._serialized_start=121
  _globals['_DEVICE']._serialized_end=227
  _globals['_SETDEVICECOMMAND']._serialized_start=229
  _globals['_SETDEVICECOMMAND']._serialized_end=294
  _globals['_LOGINCOMMAND']._serialized_start=297
  _globals['_LOGINCOMMAND']._serialized_end=633
  _globals['_LOGINCOMMAND_INNERLOGINCOMMAND']._serialized_start=365
  _globals['_LOGINCOMMAND_INNERLOGINCOMMAND']._serialized_end=633
  _globals['_LOGINCOMMAND_INNERLOGINCOMMAND_UNKNOWNINNER']._serialized_start=587
  _globals['_LOGINCOMMAND_INNERLOGINCOMMAND_UNKNOWNINNER']._serialized_end=633
# @@protoc_insertion_point(module_scope)
