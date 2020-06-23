# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/monitoring_dashboard_v1/proto/text.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/monitoring_dashboard_v1/proto/text.proto",
    package="google.monitoring.dashboard.v1",
    syntax="proto3",
    serialized_options=b'\n"com.google.monitoring.dashboard.v1B\tTextProtoP\001ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard\352\002(Google::Cloud::Monitoring::Dashboard::V1',
    serialized_pb=b'\n5google/cloud/monitoring_dashboard_v1/proto/text.proto\x12\x1egoogle.monitoring.dashboard.v1"\x8d\x01\n\x04Text\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12;\n\x06\x66ormat\x18\x02 \x01(\x0e\x32+.google.monitoring.dashboard.v1.Text.Format"7\n\x06\x46ormat\x12\x16\n\x12\x46ORMAT_UNSPECIFIED\x10\x00\x12\x0c\n\x08MARKDOWN\x10\x01\x12\x07\n\x03RAW\x10\x02\x42\xa5\x01\n"com.google.monitoring.dashboard.v1B\tTextProtoP\x01ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3',
)


_TEXT_FORMAT = _descriptor.EnumDescriptor(
    name="Format",
    full_name="google.monitoring.dashboard.v1.Text.Format",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="FORMAT_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="MARKDOWN", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="RAW", index=2, number=2, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=176,
    serialized_end=231,
)
_sym_db.RegisterEnumDescriptor(_TEXT_FORMAT)


_TEXT = _descriptor.Descriptor(
    name="Text",
    full_name="google.monitoring.dashboard.v1.Text",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="content",
            full_name="google.monitoring.dashboard.v1.Text.content",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="format",
            full_name="google.monitoring.dashboard.v1.Text.format",
            index=1,
            number=2,
            type=14,
            cpp_type=8,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_TEXT_FORMAT,],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=90,
    serialized_end=231,
)

_TEXT.fields_by_name["format"].enum_type = _TEXT_FORMAT
_TEXT_FORMAT.containing_type = _TEXT
DESCRIPTOR.message_types_by_name["Text"] = _TEXT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Text = _reflection.GeneratedProtocolMessageType(
    "Text",
    (_message.Message,),
    {
        "DESCRIPTOR": _TEXT,
        "__module__": "google.cloud.monitoring_dashboard.v1.proto.text_pb2",
        "__doc__": """A widget that displays textual content.
  
  
  Attributes:
      content:
          The text content to be displayed.
      format:
          How the text content is formatted.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.Text)
    },
)
_sym_db.RegisterMessage(Text)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
