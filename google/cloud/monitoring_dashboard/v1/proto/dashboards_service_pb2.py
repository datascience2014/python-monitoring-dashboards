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
# source: google/cloud/monitoring_dashboard_v1/proto/dashboards_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.cloud.monitoring_dashboard.v1.proto import (
    dashboard_pb2 as google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_dashboard__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/monitoring_dashboard_v1/proto/dashboards_service.proto",
    package="google.monitoring.dashboard.v1",
    syntax="proto3",
    serialized_options=b'\n"com.google.monitoring.dashboard.v1B\026DashboardsServiceProtoP\001ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard\352\002(Google::Cloud::Monitoring::Dashboard::V1',
    serialized_pb=b'\nCgoogle/cloud/monitoring_dashboard_v1/proto/dashboards_service.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a:google/cloud/monitoring_dashboard_v1/proto/dashboard.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/api/client.proto"p\n\x16\x43reateDashboardRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x41\n\tdashboard\x18\x02 \x01(\x0b\x32).google.monitoring.dashboard.v1.DashboardB\x03\xe0\x41\x02"S\n\x15ListDashboardsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"p\n\x16ListDashboardsResponse\x12=\n\ndashboards\x18\x01 \x03(\x0b\x32).google.monitoring.dashboard.v1.Dashboard\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"(\n\x13GetDashboardRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0\x41\x02"+\n\x16\x44\x65leteDashboardRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0\x41\x02"[\n\x16UpdateDashboardRequest\x12\x41\n\tdashboard\x18\x01 \x01(\x0b\x32).google.monitoring.dashboard.v1.DashboardB\x03\xe0\x41\x02\x32\xb1\x08\n\x11\x44\x61shboardsService\x12\xab\x01\n\x0f\x43reateDashboard\x12\x36.google.monitoring.dashboard.v1.CreateDashboardRequest\x1a).google.monitoring.dashboard.v1.Dashboard"5\x82\xd3\xe4\x93\x02/""/v1/{parent=projects/*}/dashboards:\tdashboard\x12\xab\x01\n\x0eListDashboards\x12\x35.google.monitoring.dashboard.v1.ListDashboardsRequest\x1a\x36.google.monitoring.dashboard.v1.ListDashboardsResponse"*\x82\xd3\xe4\x93\x02$\x12"/v1/{parent=projects/*}/dashboards\x12\x9a\x01\n\x0cGetDashboard\x12\x33.google.monitoring.dashboard.v1.GetDashboardRequest\x1a).google.monitoring.dashboard.v1.Dashboard"*\x82\xd3\xe4\x93\x02$\x12"/v1/{name=projects/*/dashboards/*}\x12\x8d\x01\n\x0f\x44\x65leteDashboard\x12\x36.google.monitoring.dashboard.v1.DeleteDashboardRequest\x1a\x16.google.protobuf.Empty"*\x82\xd3\xe4\x93\x02$*"/v1/{name=projects/*/dashboards/*}\x12\xb5\x01\n\x0fUpdateDashboard\x12\x36.google.monitoring.dashboard.v1.UpdateDashboardRequest\x1a).google.monitoring.dashboard.v1.Dashboard"?\x82\xd3\xe4\x93\x02\x39\x32,/v1/{dashboard.name=projects/*/dashboards/*}:\tdashboard\x1a\xda\x01\xca\x41\x19monitoring.googleapis.com\xd2\x41\xba\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.read,https://www.googleapis.com/auth/monitoring.writeB\xb2\x01\n"com.google.monitoring.dashboard.v1B\x16\x44\x61shboardsServiceProtoP\x01ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3',
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_dashboard__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,
        google_dot_api_dot_client__pb2.DESCRIPTOR,
    ],
)


_CREATEDASHBOARDREQUEST = _descriptor.Descriptor(
    name="CreateDashboardRequest",
    full_name="google.monitoring.dashboard.v1.CreateDashboardRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.monitoring.dashboard.v1.CreateDashboardRequest.parent",
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
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="dashboard",
            full_name="google.monitoring.dashboard.v1.CreateDashboardRequest.dashboard",
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
            serialized_options=b"\340A\002",
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
    serialized_start=314,
    serialized_end=426,
)


_LISTDASHBOARDSREQUEST = _descriptor.Descriptor(
    name="ListDashboardsRequest",
    full_name="google.monitoring.dashboard.v1.ListDashboardsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.monitoring.dashboard.v1.ListDashboardsRequest.parent",
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
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="page_size",
            full_name="google.monitoring.dashboard.v1.ListDashboardsRequest.page_size",
            index=1,
            number=2,
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
            name="page_token",
            full_name="google.monitoring.dashboard.v1.ListDashboardsRequest.page_token",
            index=2,
            number=3,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=428,
    serialized_end=511,
)


_LISTDASHBOARDSRESPONSE = _descriptor.Descriptor(
    name="ListDashboardsResponse",
    full_name="google.monitoring.dashboard.v1.ListDashboardsResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="dashboards",
            full_name="google.monitoring.dashboard.v1.ListDashboardsResponse.dashboards",
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
        _descriptor.FieldDescriptor(
            name="next_page_token",
            full_name="google.monitoring.dashboard.v1.ListDashboardsResponse.next_page_token",
            index=1,
            number=2,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=513,
    serialized_end=625,
)


_GETDASHBOARDREQUEST = _descriptor.Descriptor(
    name="GetDashboardRequest",
    full_name="google.monitoring.dashboard.v1.GetDashboardRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.monitoring.dashboard.v1.GetDashboardRequest.name",
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
            serialized_options=b"\340A\002",
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
    serialized_start=627,
    serialized_end=667,
)


_DELETEDASHBOARDREQUEST = _descriptor.Descriptor(
    name="DeleteDashboardRequest",
    full_name="google.monitoring.dashboard.v1.DeleteDashboardRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.monitoring.dashboard.v1.DeleteDashboardRequest.name",
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
            serialized_options=b"\340A\002",
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
    serialized_start=669,
    serialized_end=712,
)


_UPDATEDASHBOARDREQUEST = _descriptor.Descriptor(
    name="UpdateDashboardRequest",
    full_name="google.monitoring.dashboard.v1.UpdateDashboardRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="dashboard",
            full_name="google.monitoring.dashboard.v1.UpdateDashboardRequest.dashboard",
            index=0,
            number=1,
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
            serialized_options=b"\340A\002",
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
    serialized_start=714,
    serialized_end=805,
)

_CREATEDASHBOARDREQUEST.fields_by_name[
    "dashboard"
].message_type = (
    google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_dashboard__pb2._DASHBOARD
)
_LISTDASHBOARDSRESPONSE.fields_by_name[
    "dashboards"
].message_type = (
    google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_dashboard__pb2._DASHBOARD
)
_UPDATEDASHBOARDREQUEST.fields_by_name[
    "dashboard"
].message_type = (
    google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_dashboard__pb2._DASHBOARD
)
DESCRIPTOR.message_types_by_name["CreateDashboardRequest"] = _CREATEDASHBOARDREQUEST
DESCRIPTOR.message_types_by_name["ListDashboardsRequest"] = _LISTDASHBOARDSREQUEST
DESCRIPTOR.message_types_by_name["ListDashboardsResponse"] = _LISTDASHBOARDSRESPONSE
DESCRIPTOR.message_types_by_name["GetDashboardRequest"] = _GETDASHBOARDREQUEST
DESCRIPTOR.message_types_by_name["DeleteDashboardRequest"] = _DELETEDASHBOARDREQUEST
DESCRIPTOR.message_types_by_name["UpdateDashboardRequest"] = _UPDATEDASHBOARDREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateDashboardRequest = _reflection.GeneratedProtocolMessageType(
    "CreateDashboardRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEDASHBOARDREQUEST,
        "__module__": "google.cloud.monitoring_dashboard.v1.proto.dashboards_service_pb2",
        "__doc__": """The ``CreateDashboard`` request.
  
  
  Attributes:
      parent:
          Required. The project on which to execute the request. The
          format is ``"projects/{project_id_or_number}"``. The
          {project_id_or_number} must match the dashboard resource name.
      dashboard:
          Required. The initial dashboard specification.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.CreateDashboardRequest)
    },
)
_sym_db.RegisterMessage(CreateDashboardRequest)

ListDashboardsRequest = _reflection.GeneratedProtocolMessageType(
    "ListDashboardsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTDASHBOARDSREQUEST,
        "__module__": "google.cloud.monitoring_dashboard.v1.proto.dashboards_service_pb2",
        "__doc__": """The ``ListDashboards`` request.
  
  
  Attributes:
      parent:
          Required. The scope of the dashboards to list. A project scope
          must be specified in the form of
          ``"projects/{project_id_or_number}"``.
      page_size:
          A positive number that is the maximum number of results to
          return. If unspecified, a default of 1000 is used.
      page_token:
          If this field is not empty then it must contain the
          ``nextPageToken`` value returned by a previous call to this
          method. Using this field causes the method to return
          additional results from the previous method call.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.ListDashboardsRequest)
    },
)
_sym_db.RegisterMessage(ListDashboardsRequest)

ListDashboardsResponse = _reflection.GeneratedProtocolMessageType(
    "ListDashboardsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTDASHBOARDSRESPONSE,
        "__module__": "google.cloud.monitoring_dashboard.v1.proto.dashboards_service_pb2",
        "__doc__": """The ``ListDashboards`` request.
  
  
  Attributes:
      dashboards:
          The list of requested dashboards.
      next_page_token:
          If there are more results than have been returned, then this
          field is set to a non-empty value. To see the additional
          results, use that value as ``pageToken`` in the next call to
          this method.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.ListDashboardsResponse)
    },
)
_sym_db.RegisterMessage(ListDashboardsResponse)

GetDashboardRequest = _reflection.GeneratedProtocolMessageType(
    "GetDashboardRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETDASHBOARDREQUEST,
        "__module__": "google.cloud.monitoring_dashboard.v1.proto.dashboards_service_pb2",
        "__doc__": """The ``GetDashboard`` request.
  
  
  Attributes:
      name:
          Required. The resource name of the Dashboard. The format is
          one of ``"dashboards/{dashboard_id}"`` (for system dashboards)
          or ``"projects/{project_id_or_number}/dashboards/{dashboard_id
          }"`` (for custom dashboards).
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.GetDashboardRequest)
    },
)
_sym_db.RegisterMessage(GetDashboardRequest)

DeleteDashboardRequest = _reflection.GeneratedProtocolMessageType(
    "DeleteDashboardRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETEDASHBOARDREQUEST,
        "__module__": "google.cloud.monitoring_dashboard.v1.proto.dashboards_service_pb2",
        "__doc__": """The ``DeleteDashboard`` request.
  
  
  Attributes:
      name:
          Required. The resource name of the Dashboard. The format is
          ``"projects/{project_id_or_number}/dashboards/{dashboard_id}"``.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.DeleteDashboardRequest)
    },
)
_sym_db.RegisterMessage(DeleteDashboardRequest)

UpdateDashboardRequest = _reflection.GeneratedProtocolMessageType(
    "UpdateDashboardRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATEDASHBOARDREQUEST,
        "__module__": "google.cloud.monitoring_dashboard.v1.proto.dashboards_service_pb2",
        "__doc__": """The ``UpdateDashboard`` request.
  
  
  Attributes:
      dashboard:
          Required. The dashboard that will replace the existing
          dashboard.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.UpdateDashboardRequest)
    },
)
_sym_db.RegisterMessage(UpdateDashboardRequest)


DESCRIPTOR._options = None
_CREATEDASHBOARDREQUEST.fields_by_name["parent"]._options = None
_CREATEDASHBOARDREQUEST.fields_by_name["dashboard"]._options = None
_LISTDASHBOARDSREQUEST.fields_by_name["parent"]._options = None
_GETDASHBOARDREQUEST.fields_by_name["name"]._options = None
_DELETEDASHBOARDREQUEST.fields_by_name["name"]._options = None
_UPDATEDASHBOARDREQUEST.fields_by_name["dashboard"]._options = None

_DASHBOARDSSERVICE = _descriptor.ServiceDescriptor(
    name="DashboardsService",
    full_name="google.monitoring.dashboard.v1.DashboardsService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=b"\312A\031monitoring.googleapis.com\322A\272\001https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.read,https://www.googleapis.com/auth/monitoring.write",
    serialized_start=808,
    serialized_end=1881,
    methods=[
        _descriptor.MethodDescriptor(
            name="CreateDashboard",
            full_name="google.monitoring.dashboard.v1.DashboardsService.CreateDashboard",
            index=0,
            containing_service=None,
            input_type=_CREATEDASHBOARDREQUEST,
            output_type=google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_dashboard__pb2._DASHBOARD,
            serialized_options=b'\202\323\344\223\002/""/v1/{parent=projects/*}/dashboards:\tdashboard',
        ),
        _descriptor.MethodDescriptor(
            name="ListDashboards",
            full_name="google.monitoring.dashboard.v1.DashboardsService.ListDashboards",
            index=1,
            containing_service=None,
            input_type=_LISTDASHBOARDSREQUEST,
            output_type=_LISTDASHBOARDSRESPONSE,
            serialized_options=b'\202\323\344\223\002$\022"/v1/{parent=projects/*}/dashboards',
        ),
        _descriptor.MethodDescriptor(
            name="GetDashboard",
            full_name="google.monitoring.dashboard.v1.DashboardsService.GetDashboard",
            index=2,
            containing_service=None,
            input_type=_GETDASHBOARDREQUEST,
            output_type=google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_dashboard__pb2._DASHBOARD,
            serialized_options=b'\202\323\344\223\002$\022"/v1/{name=projects/*/dashboards/*}',
        ),
        _descriptor.MethodDescriptor(
            name="DeleteDashboard",
            full_name="google.monitoring.dashboard.v1.DashboardsService.DeleteDashboard",
            index=3,
            containing_service=None,
            input_type=_DELETEDASHBOARDREQUEST,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=b'\202\323\344\223\002$*"/v1/{name=projects/*/dashboards/*}',
        ),
        _descriptor.MethodDescriptor(
            name="UpdateDashboard",
            full_name="google.monitoring.dashboard.v1.DashboardsService.UpdateDashboard",
            index=4,
            containing_service=None,
            input_type=_UPDATEDASHBOARDREQUEST,
            output_type=google_dot_cloud_dot_monitoring__dashboard__v1_dot_proto_dot_dashboard__pb2._DASHBOARD,
            serialized_options=b"\202\323\344\223\00292,/v1/{dashboard.name=projects/*/dashboards/*}:\tdashboard",
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_DASHBOARDSSERVICE)

DESCRIPTOR.services_by_name["DashboardsService"] = _DASHBOARDSSERVICE

# @@protoc_insertion_point(module_scope)
