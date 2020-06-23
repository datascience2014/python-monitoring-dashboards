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
# source: google/cloud/monitoring_dashboard_v1/proto/layouts.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.monitoring_dashboard.v1.proto import (
    widget_pb2 as google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_widget__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/monitoring_dashboard_v1/proto/layouts.proto",
    package="google.monitoring.dashboard.v1",
    syntax="proto3",
    serialized_options=b'\n"com.google.monitoring.dashboard.v1B\014LayoutsProtoP\001ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard\352\002(Google::Cloud::Monitoring::Dashboard::V1',
    serialized_pb=b'\n8google/cloud/monitoring_dashboard_v1/proto/layouts.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a\x37google/cloud/monitoring_dashboard_v1/proto/widget.proto"V\n\nGridLayout\x12\x0f\n\x07\x63olumns\x18\x01 \x01(\x03\x12\x37\n\x07widgets\x18\x02 \x03(\x0b\x32&.google.monitoring.dashboard.v1.Widget"\x98\x01\n\tRowLayout\x12;\n\x04rows\x18\x01 \x03(\x0b\x32-.google.monitoring.dashboard.v1.RowLayout.Row\x1aN\n\x03Row\x12\x0e\n\x06weight\x18\x01 \x01(\x03\x12\x37\n\x07widgets\x18\x02 \x03(\x0b\x32&.google.monitoring.dashboard.v1.Widget"\xa7\x01\n\x0c\x43olumnLayout\x12\x44\n\x07\x63olumns\x18\x01 \x03(\x0b\x32\x33.google.monitoring.dashboard.v1.ColumnLayout.Column\x1aQ\n\x06\x43olumn\x12\x0e\n\x06weight\x18\x01 \x01(\x03\x12\x37\n\x07widgets\x18\x02 \x03(\x0b\x32&.google.monitoring.dashboard.v1.WidgetB\xa8\x01\n"com.google.monitoring.dashboard.v1B\x0cLayoutsProtoP\x01ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3',
    dependencies=[
        google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_widget__pb2.DESCRIPTOR,
    ],
)


_GRIDLAYOUT = _descriptor.Descriptor(
    name="GridLayout",
    full_name="google.monitoring.dashboard.v1.GridLayout",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="columns",
            full_name="google.monitoring.dashboard.v1.GridLayout.columns",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
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
            name="widgets",
            full_name="google.monitoring.dashboard.v1.GridLayout.widgets",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
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
    serialized_start=149,
    serialized_end=235,
)


_ROWLAYOUT_ROW = _descriptor.Descriptor(
    name="Row",
    full_name="google.monitoring.dashboard.v1.RowLayout.Row",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="weight",
            full_name="google.monitoring.dashboard.v1.RowLayout.Row.weight",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
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
            name="widgets",
            full_name="google.monitoring.dashboard.v1.RowLayout.Row.widgets",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
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
    serialized_start=312,
    serialized_end=390,
)

_ROWLAYOUT = _descriptor.Descriptor(
    name="RowLayout",
    full_name="google.monitoring.dashboard.v1.RowLayout",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="rows",
            full_name="google.monitoring.dashboard.v1.RowLayout.rows",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
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
    nested_types=[_ROWLAYOUT_ROW,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=238,
    serialized_end=390,
)


_COLUMNLAYOUT_COLUMN = _descriptor.Descriptor(
    name="Column",
    full_name="google.monitoring.dashboard.v1.ColumnLayout.Column",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="weight",
            full_name="google.monitoring.dashboard.v1.ColumnLayout.Column.weight",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
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
            name="widgets",
            full_name="google.monitoring.dashboard.v1.ColumnLayout.Column.widgets",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
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
    serialized_start=479,
    serialized_end=560,
)

_COLUMNLAYOUT = _descriptor.Descriptor(
    name="ColumnLayout",
    full_name="google.monitoring.dashboard.v1.ColumnLayout",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="columns",
            full_name="google.monitoring.dashboard.v1.ColumnLayout.columns",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
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
    nested_types=[_COLUMNLAYOUT_COLUMN,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=393,
    serialized_end=560,
)

_GRIDLAYOUT.fields_by_name[
    "widgets"
].message_type = (
    google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_widget__pb2._WIDGET
)
_ROWLAYOUT_ROW.fields_by_name[
    "widgets"
].message_type = (
    google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_widget__pb2._WIDGET
)
_ROWLAYOUT_ROW.containing_type = _ROWLAYOUT
_ROWLAYOUT.fields_by_name["rows"].message_type = _ROWLAYOUT_ROW
_COLUMNLAYOUT_COLUMN.fields_by_name[
    "widgets"
].message_type = (
    google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_widget__pb2._WIDGET
)
_COLUMNLAYOUT_COLUMN.containing_type = _COLUMNLAYOUT
_COLUMNLAYOUT.fields_by_name["columns"].message_type = _COLUMNLAYOUT_COLUMN
DESCRIPTOR.message_types_by_name["GridLayout"] = _GRIDLAYOUT
DESCRIPTOR.message_types_by_name["RowLayout"] = _ROWLAYOUT
DESCRIPTOR.message_types_by_name["ColumnLayout"] = _COLUMNLAYOUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GridLayout = _reflection.GeneratedProtocolMessageType(
    "GridLayout",
    (_message.Message,),
    {
        "DESCRIPTOR": _GRIDLAYOUT,
        "__module__": "google.cloud.monitoring_dashboard.v1.proto.layouts_pb2",
        "__doc__": """A basic layout divides the available space into vertical columns of
  equal width and arranges a list of widgets using a row-first strategy.
  Attributes:
      columns:
          The number of columns into which the view’s width is divided.
          If omitted or set to zero, a system default will be used while
          rendering.
      widgets:
          The informational elements that are arranged into the columns
          row-first.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.GridLayout)
    },
)
_sym_db.RegisterMessage(GridLayout)

RowLayout = _reflection.GeneratedProtocolMessageType(
    "RowLayout",
    (_message.Message,),
    {
        "Row": _reflection.GeneratedProtocolMessageType(
            "Row",
            (_message.Message,),
            {
                "DESCRIPTOR": _ROWLAYOUT_ROW,
                "__module__": "google.cloud.monitoring_dashboard.v1.proto.layouts_pb2",
                "__doc__": """Defines the layout properties and content for a row.
    Attributes:
        weight:
            The relative weight of this row. The row weight is used to
            adjust the height of rows on the screen (relative to peers).
            Greater the weight, greater the height of the row on the
            screen. If omitted, a value of 1 is used while rendering.
        widgets:
            The display widgets arranged horizontally in this row.
    """,
                # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.RowLayout.Row)
            },
        ),
        "DESCRIPTOR": _ROWLAYOUT,
        "__module__": "google.cloud.monitoring_dashboard.v1.proto.layouts_pb2",
        "__doc__": """A simplified layout that divides the available space into rows and
  arranges a set of widgets horizontally in each row.
  Attributes:
      rows:
          The rows of content to display.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.RowLayout)
    },
)
_sym_db.RegisterMessage(RowLayout)
_sym_db.RegisterMessage(RowLayout.Row)

ColumnLayout = _reflection.GeneratedProtocolMessageType(
    "ColumnLayout",
    (_message.Message,),
    {
        "Column": _reflection.GeneratedProtocolMessageType(
            "Column",
            (_message.Message,),
            {
                "DESCRIPTOR": _COLUMNLAYOUT_COLUMN,
                "__module__": "google.cloud.monitoring_dashboard.v1.proto.layouts_pb2",
                "__doc__": """Defines the layout properties and content for a column.
    Attributes:
        weight:
            The relative weight of this column. The column weight is used
            to adjust the width of columns on the screen (relative to
            peers). Greater the weight, greater the width of the column on
            the screen. If omitted, a value of 1 is used while rendering.
        widgets:
            The display widgets arranged vertically in this column.
    """,
                # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.ColumnLayout.Column)
            },
        ),
        "DESCRIPTOR": _COLUMNLAYOUT,
        "__module__": "google.cloud.monitoring_dashboard.v1.proto.layouts_pb2",
        "__doc__": """A simplified layout that divides the available space into vertical
  columns and arranges a set of widgets vertically in each column.
  Attributes:
      columns:
          The columns of content to display.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.ColumnLayout)
    },
)
_sym_db.RegisterMessage(ColumnLayout)
_sym_db.RegisterMessage(ColumnLayout.Column)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
