# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/bigtable/admin_v2/proto/common.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/bigtable/admin_v2/proto/common.proto",
    package="google.bigtable.admin.v2",
    syntax="proto3",
    serialized_options=_b(
        "\n\034com.google.bigtable.admin.v2B\013CommonProtoP\001Z=google.golang.org/genproto/googleapis/bigtable/admin/v2;admin\252\002\036Google.Cloud.Bigtable.Admin.V2\312\002\036Google\\Cloud\\Bigtable\\Admin\\V2"
    ),
    serialized_pb=_b(
        '\n1google/cloud/bigtable/admin_v2/proto/common.proto\x12\x18google.bigtable.admin.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8b\x01\n\x11OperationProgress\x12\x18\n\x10progress_percent\x18\x01 \x01(\x05\x12.\n\nstart_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp*=\n\x0bStorageType\x12\x1c\n\x18STORAGE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03SSD\x10\x01\x12\x07\n\x03HDD\x10\x02\x42\xae\x01\n\x1c\x63om.google.bigtable.admin.v2B\x0b\x43ommonProtoP\x01Z=google.golang.org/genproto/googleapis/bigtable/admin/v2;admin\xaa\x02\x1eGoogle.Cloud.Bigtable.Admin.V2\xca\x02\x1eGoogle\\Cloud\\Bigtable\\Admin\\V2b\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
    ],
)

_STORAGETYPE = _descriptor.EnumDescriptor(
    name="StorageType",
    full_name="google.bigtable.admin.v2.StorageType",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="STORAGE_TYPE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="SSD", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="HDD", index=2, number=2, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=284,
    serialized_end=345,
)
_sym_db.RegisterEnumDescriptor(_STORAGETYPE)

StorageType = enum_type_wrapper.EnumTypeWrapper(_STORAGETYPE)
STORAGE_TYPE_UNSPECIFIED = 0
SSD = 1
HDD = 2


_OPERATIONPROGRESS = _descriptor.Descriptor(
    name="OperationProgress",
    full_name="google.bigtable.admin.v2.OperationProgress",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="progress_percent",
            full_name="google.bigtable.admin.v2.OperationProgress.progress_percent",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="start_time",
            full_name="google.bigtable.admin.v2.OperationProgress.start_time",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="end_time",
            full_name="google.bigtable.admin.v2.OperationProgress.end_time",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=143,
    serialized_end=282,
)

_OPERATIONPROGRESS.fields_by_name[
    "start_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_OPERATIONPROGRESS.fields_by_name[
    "end_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name["OperationProgress"] = _OPERATIONPROGRESS
DESCRIPTOR.enum_types_by_name["StorageType"] = _STORAGETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OperationProgress = _reflection.GeneratedProtocolMessageType(
    "OperationProgress",
    (_message.Message,),
    dict(
        DESCRIPTOR=_OPERATIONPROGRESS,
        __module__="google.cloud.bigtable.admin_v2.proto.common_pb2",
        __doc__="""Encapsulates progress related information for a Cloud Bigtable long
  running operation.
  
  
  Attributes:
      progress_percent:
          Percent completion of the operation. Values are between 0 and
          100 inclusive.
      start_time:
          Time the request was received.
      end_time:
          If set, the time at which this operation failed or was
          completed successfully.
  """,
        # @@protoc_insertion_point(class_scope:google.bigtable.admin.v2.OperationProgress)
    ),
)
_sym_db.RegisterMessage(OperationProgress)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
