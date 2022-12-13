# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/streetview/publish_v1/proto/rpcmessages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.streetview.publish_v1.proto import resources_pb2 as google_dot_streetview_dot_publish__v1_dot_proto_dot_resources__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/streetview/publish_v1/proto/rpcmessages.proto',
  package='google.streetview.publish.v1',
  syntax='proto3',
  serialized_options=_b('\n(com.google.geo.ugc.streetview.publish.v1B\034StreetViewPublishRpcMessagesZCgoogle.golang.org/genproto/googleapis/streetview/publish/v1;publish'),
  serialized_pb=_b('\n4google/streetview/publish_v1/proto/rpcmessages.proto\x12\x1cgoogle.streetview.publish.v1\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto\x1a\x32google/streetview/publish_v1/proto/resources.proto\"H\n\x12\x43reatePhotoRequest\x12\x32\n\x05photo\x18\x01 \x01(\x0b\x32#.google.streetview.publish.v1.Photo\"q\n\x0fGetPhotoRequest\x12\x10\n\x08photo_id\x18\x01 \x01(\t\x12\x35\n\x04view\x18\x02 \x01(\x0e\x32\'.google.streetview.publish.v1.PhotoView\x12\x15\n\rlanguage_code\x18\x03 \x01(\t\"x\n\x15\x42\x61tchGetPhotosRequest\x12\x11\n\tphoto_ids\x18\x01 \x03(\t\x12\x35\n\x04view\x18\x02 \x01(\x0e\x32\'.google.streetview.publish.v1.PhotoView\x12\x15\n\rlanguage_code\x18\x03 \x01(\t\"V\n\x16\x42\x61tchGetPhotosResponse\x12<\n\x07results\x18\x01 \x03(\x0b\x32+.google.streetview.publish.v1.PhotoResponse\"g\n\rPhotoResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\x12\x32\n\x05photo\x18\x02 \x01(\x0b\x32#.google.streetview.publish.v1.Photo\"\x98\x01\n\x11ListPhotosRequest\x12\x35\n\x04view\x18\x01 \x01(\x0e\x32\'.google.streetview.publish.v1.PhotoView\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\x12\x15\n\rlanguage_code\x18\x05 \x01(\t\"b\n\x12ListPhotosResponse\x12\x33\n\x06photos\x18\x01 \x03(\x0b\x32#.google.streetview.publish.v1.Photo\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"y\n\x12UpdatePhotoRequest\x12\x32\n\x05photo\x18\x01 \x01(\x0b\x32#.google.streetview.publish.v1.Photo\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"k\n\x18\x42\x61tchUpdatePhotosRequest\x12O\n\x15update_photo_requests\x18\x01 \x03(\x0b\x32\x30.google.streetview.publish.v1.UpdatePhotoRequest\"Y\n\x19\x42\x61tchUpdatePhotosResponse\x12<\n\x07results\x18\x01 \x03(\x0b\x32+.google.streetview.publish.v1.PhotoResponse\"&\n\x12\x44\x65letePhotoRequest\x12\x10\n\x08photo_id\x18\x01 \x01(\t\"-\n\x18\x42\x61tchDeletePhotosRequest\x12\x11\n\tphoto_ids\x18\x01 \x03(\t\"?\n\x19\x42\x61tchDeletePhotosResponse\x12\"\n\x06status\x18\x01 \x03(\x0b\x32\x12.google.rpc.Status*0\n\tPhotoView\x12\t\n\x05\x42\x41SIC\x10\x00\x12\x18\n\x14INCLUDE_DOWNLOAD_URL\x10\x01\x42\x8d\x01\n(com.google.geo.ugc.streetview.publish.v1B\x1cStreetViewPublishRpcMessagesZCgoogle.golang.org/genproto/googleapis/streetview/publish/v1;publishb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,google_dot_streetview_dot_publish__v1_dot_proto_dot_resources__pb2.DESCRIPTOR,])

_PHOTOVIEW = _descriptor.EnumDescriptor(
  name='PhotoView',
  full_name='google.streetview.publish.v1.PhotoView',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BASIC', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCLUDE_DOWNLOAD_URL', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1431,
  serialized_end=1479,
)
_sym_db.RegisterEnumDescriptor(_PHOTOVIEW)

PhotoView = enum_type_wrapper.EnumTypeWrapper(_PHOTOVIEW)
BASIC = 0
INCLUDE_DOWNLOAD_URL = 1



_CREATEPHOTOREQUEST = _descriptor.Descriptor(
  name='CreatePhotoRequest',
  full_name='google.streetview.publish.v1.CreatePhotoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='photo', full_name='google.streetview.publish.v1.CreatePhotoRequest.photo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=269,
)


_GETPHOTOREQUEST = _descriptor.Descriptor(
  name='GetPhotoRequest',
  full_name='google.streetview.publish.v1.GetPhotoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='photo_id', full_name='google.streetview.publish.v1.GetPhotoRequest.photo_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='view', full_name='google.streetview.publish.v1.GetPhotoRequest.view', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language_code', full_name='google.streetview.publish.v1.GetPhotoRequest.language_code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=271,
  serialized_end=384,
)


_BATCHGETPHOTOSREQUEST = _descriptor.Descriptor(
  name='BatchGetPhotosRequest',
  full_name='google.streetview.publish.v1.BatchGetPhotosRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='photo_ids', full_name='google.streetview.publish.v1.BatchGetPhotosRequest.photo_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='view', full_name='google.streetview.publish.v1.BatchGetPhotosRequest.view', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language_code', full_name='google.streetview.publish.v1.BatchGetPhotosRequest.language_code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=386,
  serialized_end=506,
)


_BATCHGETPHOTOSRESPONSE = _descriptor.Descriptor(
  name='BatchGetPhotosResponse',
  full_name='google.streetview.publish.v1.BatchGetPhotosResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='google.streetview.publish.v1.BatchGetPhotosResponse.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=508,
  serialized_end=594,
)


_PHOTORESPONSE = _descriptor.Descriptor(
  name='PhotoResponse',
  full_name='google.streetview.publish.v1.PhotoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='google.streetview.publish.v1.PhotoResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='photo', full_name='google.streetview.publish.v1.PhotoResponse.photo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=596,
  serialized_end=699,
)


_LISTPHOTOSREQUEST = _descriptor.Descriptor(
  name='ListPhotosRequest',
  full_name='google.streetview.publish.v1.ListPhotosRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='view', full_name='google.streetview.publish.v1.ListPhotosRequest.view', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.streetview.publish.v1.ListPhotosRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.streetview.publish.v1.ListPhotosRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='google.streetview.publish.v1.ListPhotosRequest.filter', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language_code', full_name='google.streetview.publish.v1.ListPhotosRequest.language_code', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=702,
  serialized_end=854,
)


_LISTPHOTOSRESPONSE = _descriptor.Descriptor(
  name='ListPhotosResponse',
  full_name='google.streetview.publish.v1.ListPhotosResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='photos', full_name='google.streetview.publish.v1.ListPhotosResponse.photos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.streetview.publish.v1.ListPhotosResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=856,
  serialized_end=954,
)


_UPDATEPHOTOREQUEST = _descriptor.Descriptor(
  name='UpdatePhotoRequest',
  full_name='google.streetview.publish.v1.UpdatePhotoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='photo', full_name='google.streetview.publish.v1.UpdatePhotoRequest.photo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.streetview.publish.v1.UpdatePhotoRequest.update_mask', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=956,
  serialized_end=1077,
)


_BATCHUPDATEPHOTOSREQUEST = _descriptor.Descriptor(
  name='BatchUpdatePhotosRequest',
  full_name='google.streetview.publish.v1.BatchUpdatePhotosRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_photo_requests', full_name='google.streetview.publish.v1.BatchUpdatePhotosRequest.update_photo_requests', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1079,
  serialized_end=1186,
)


_BATCHUPDATEPHOTOSRESPONSE = _descriptor.Descriptor(
  name='BatchUpdatePhotosResponse',
  full_name='google.streetview.publish.v1.BatchUpdatePhotosResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='google.streetview.publish.v1.BatchUpdatePhotosResponse.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1188,
  serialized_end=1277,
)


_DELETEPHOTOREQUEST = _descriptor.Descriptor(
  name='DeletePhotoRequest',
  full_name='google.streetview.publish.v1.DeletePhotoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='photo_id', full_name='google.streetview.publish.v1.DeletePhotoRequest.photo_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1279,
  serialized_end=1317,
)


_BATCHDELETEPHOTOSREQUEST = _descriptor.Descriptor(
  name='BatchDeletePhotosRequest',
  full_name='google.streetview.publish.v1.BatchDeletePhotosRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='photo_ids', full_name='google.streetview.publish.v1.BatchDeletePhotosRequest.photo_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1319,
  serialized_end=1364,
)


_BATCHDELETEPHOTOSRESPONSE = _descriptor.Descriptor(
  name='BatchDeletePhotosResponse',
  full_name='google.streetview.publish.v1.BatchDeletePhotosResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='google.streetview.publish.v1.BatchDeletePhotosResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1366,
  serialized_end=1429,
)

_CREATEPHOTOREQUEST.fields_by_name['photo'].message_type = google_dot_streetview_dot_publish__v1_dot_proto_dot_resources__pb2._PHOTO
_GETPHOTOREQUEST.fields_by_name['view'].enum_type = _PHOTOVIEW
_BATCHGETPHOTOSREQUEST.fields_by_name['view'].enum_type = _PHOTOVIEW
_BATCHGETPHOTOSRESPONSE.fields_by_name['results'].message_type = _PHOTORESPONSE
_PHOTORESPONSE.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_PHOTORESPONSE.fields_by_name['photo'].message_type = google_dot_streetview_dot_publish__v1_dot_proto_dot_resources__pb2._PHOTO
_LISTPHOTOSREQUEST.fields_by_name['view'].enum_type = _PHOTOVIEW
_LISTPHOTOSRESPONSE.fields_by_name['photos'].message_type = google_dot_streetview_dot_publish__v1_dot_proto_dot_resources__pb2._PHOTO
_UPDATEPHOTOREQUEST.fields_by_name['photo'].message_type = google_dot_streetview_dot_publish__v1_dot_proto_dot_resources__pb2._PHOTO
_UPDATEPHOTOREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_BATCHUPDATEPHOTOSREQUEST.fields_by_name['update_photo_requests'].message_type = _UPDATEPHOTOREQUEST
_BATCHUPDATEPHOTOSRESPONSE.fields_by_name['results'].message_type = _PHOTORESPONSE
_BATCHDELETEPHOTOSRESPONSE.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
DESCRIPTOR.message_types_by_name['CreatePhotoRequest'] = _CREATEPHOTOREQUEST
DESCRIPTOR.message_types_by_name['GetPhotoRequest'] = _GETPHOTOREQUEST
DESCRIPTOR.message_types_by_name['BatchGetPhotosRequest'] = _BATCHGETPHOTOSREQUEST
DESCRIPTOR.message_types_by_name['BatchGetPhotosResponse'] = _BATCHGETPHOTOSRESPONSE
DESCRIPTOR.message_types_by_name['PhotoResponse'] = _PHOTORESPONSE
DESCRIPTOR.message_types_by_name['ListPhotosRequest'] = _LISTPHOTOSREQUEST
DESCRIPTOR.message_types_by_name['ListPhotosResponse'] = _LISTPHOTOSRESPONSE
DESCRIPTOR.message_types_by_name['UpdatePhotoRequest'] = _UPDATEPHOTOREQUEST
DESCRIPTOR.message_types_by_name['BatchUpdatePhotosRequest'] = _BATCHUPDATEPHOTOSREQUEST
DESCRIPTOR.message_types_by_name['BatchUpdatePhotosResponse'] = _BATCHUPDATEPHOTOSRESPONSE
DESCRIPTOR.message_types_by_name['DeletePhotoRequest'] = _DELETEPHOTOREQUEST
DESCRIPTOR.message_types_by_name['BatchDeletePhotosRequest'] = _BATCHDELETEPHOTOSREQUEST
DESCRIPTOR.message_types_by_name['BatchDeletePhotosResponse'] = _BATCHDELETEPHOTOSRESPONSE
DESCRIPTOR.enum_types_by_name['PhotoView'] = _PHOTOVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreatePhotoRequest = _reflection.GeneratedProtocolMessageType('CreatePhotoRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEPHOTOREQUEST,
  __module__ = 'google.streetview.publish_v1.proto.rpcmessages_pb2'
  ,
  __doc__ = """Request to create a [Photo][google.streetview.publish.v1.Photo].
  
  
  Attributes:
      photo:
          Required. Photo to create.
  """,
  # @@protoc_insertion_point(class_scope:google.streetview.publish.v1.CreatePhotoRequest)
  ))
_sym_db.RegisterMessage(CreatePhotoRequest)

GetPhotoRequest = _reflection.GeneratedProtocolMessageType('GetPhotoRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPHOTOREQUEST,
  __module__ = 'google.streetview.publish_v1.proto.rpcmessages_pb2'
  ,
  __doc__ = """Request to get a [Photo][google.streetview.publish.v1.Photo].
  
  By default
  
  -  does not return the download URL for the photo bytes.
  
  Parameters:
  
  -  ``view`` controls if the download URL for the photo bytes is
     returned.
  
  
  Attributes:
      photo_id:
          Required. ID of the
          [Photo][google.streetview.publish.v1.Photo].
      view:
          Specifies if a download URL for the photo bytes should be
          returned in the [Photo][google.streetview.publish.v1.Photo]
          response.
      language_code:
          The BCP-47 language code, such as "en-US" or "sr-Latn". For
          more information, see http://www.unicode.org/reports/tr35/#Uni
          code\_locale\_identifier. If language\_code is unspecified,
          the user's language preference for Google services is used.
  """,
  # @@protoc_insertion_point(class_scope:google.streetview.publish.v1.GetPhotoRequest)
  ))
_sym_db.RegisterMessage(GetPhotoRequest)

BatchGetPhotosRequest = _reflection.GeneratedProtocolMessageType('BatchGetPhotosRequest', (_message.Message,), dict(
  DESCRIPTOR = _BATCHGETPHOTOSREQUEST,
  __module__ = 'google.streetview.publish_v1.proto.rpcmessages_pb2'
  ,
  __doc__ = """Request to get one or more [Photos][google.streetview.publish.v1.Photo].
  By default
  
  -  does not return the download URL for the photo bytes.
  
  Parameters:
  
  -  ``view`` controls if the download URL for the photo bytes is
     returned.
  
  
  Attributes:
      photo_ids:
          Required. IDs of the
          [Photos][google.streetview.publish.v1.Photo]. HTTP GET
          requests require the following syntax for the URL query
          parameter: ``photoIds=<id1>&photoIds=<id2>&...``.
      view:
          Specifies if a download URL for the photo bytes should be
          returned in the Photo response.
      language_code:
          The BCP-47 language code, such as "en-US" or "sr-Latn". For
          more information, see http://www.unicode.org/reports/tr35/#Uni
          code\_locale\_identifier. If language\_code is unspecified,
          the user's language preference for Google services is used.
  """,
  # @@protoc_insertion_point(class_scope:google.streetview.publish.v1.BatchGetPhotosRequest)
  ))
_sym_db.RegisterMessage(BatchGetPhotosRequest)

BatchGetPhotosResponse = _reflection.GeneratedProtocolMessageType('BatchGetPhotosResponse', (_message.Message,), dict(
  DESCRIPTOR = _BATCHGETPHOTOSRESPONSE,
  __module__ = 'google.streetview.publish_v1.proto.rpcmessages_pb2'
  ,
  __doc__ = """Response to batch get of [Photos][google.streetview.publish.v1.Photo].
  
  
  Attributes:
      results:
          List of results for each individual
          [Photo][google.streetview.publish.v1.Photo] requested, in the
          same order as the requests in [BatchGetPhotos][google.streetvi
          ew.publish.v1.StreetViewPublishService.BatchGetPhotos].
  """,
  # @@protoc_insertion_point(class_scope:google.streetview.publish.v1.BatchGetPhotosResponse)
  ))
_sym_db.RegisterMessage(BatchGetPhotosResponse)

PhotoResponse = _reflection.GeneratedProtocolMessageType('PhotoResponse', (_message.Message,), dict(
  DESCRIPTOR = _PHOTORESPONSE,
  __module__ = 'google.streetview.publish_v1.proto.rpcmessages_pb2'
  ,
  __doc__ = """Response payload for a single
  [Photo][google.streetview.publish.v1.Photo] in batch operations
  including
  [BatchGetPhotos][google.streetview.publish.v1.StreetViewPublishService.BatchGetPhotos]
  and
  [BatchUpdatePhotos][google.streetview.publish.v1.StreetViewPublishService.BatchUpdatePhotos].
  
  
  Attributes:
      status:
          The status for the operation to get or update a single photo
          in the batch request.
      photo:
          The [Photo][google.streetview.publish.v1.Photo] resource, if
          the request was successful.
  """,
  # @@protoc_insertion_point(class_scope:google.streetview.publish.v1.PhotoResponse)
  ))
_sym_db.RegisterMessage(PhotoResponse)

ListPhotosRequest = _reflection.GeneratedProtocolMessageType('ListPhotosRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTPHOTOSREQUEST,
  __module__ = 'google.streetview.publish_v1.proto.rpcmessages_pb2'
  ,
  __doc__ = """Request to list all photos that belong to the user sending the request.
  
  By default
  
  -  does not return the download URL for the photo bytes.
  
  Parameters:
  
  -  ``view`` controls if the download URL for the photo bytes is
     returned.
  -  ``pageSize`` determines the maximum number of photos to return.
  -  ``pageToken`` is the next page token value returned from a previous
     [ListPhotos][google.streetview.publish.v1.StreetViewPublishService.ListPhotos]
     request, if any.
  -  ``filter`` allows filtering by a given parameter. 'placeId' is the
     only parameter supported at the moment.
  
  
  Attributes:
      view:
          Specifies if a download URL for the photos bytes should be
          returned in the Photos response.
      page_size:
          The maximum number of photos to return. ``pageSize`` must be
          non-negative. If ``pageSize`` is zero or is not provided, the
          default page size of 100 is used. The number of photos
          returned in the response may be less than ``pageSize`` if the
          number of photos that belong to the user is less than
          ``pageSize``.
      page_token:
          The [nextPageToken][google.streetview.publish.v1.ListPhotosRes
          ponse.next\_page\_token] value returned from a previous [ListP
          hotos][google.streetview.publish.v1.StreetViewPublishService.L
          istPhotos] request, if any.
      filter:
          The filter expression. For example:
          ``placeId=ChIJj61dQgK6j4AR4GeTYWZsKWw``.  The only filter
          supported at the moment is ``placeId``.
      language_code:
          The BCP-47 language code, such as "en-US" or "sr-Latn". For
          more information, see http://www.unicode.org/reports/tr35/#Uni
          code\_locale\_identifier. If language\_code is unspecified,
          the user's language preference for Google services is used.
  """,
  # @@protoc_insertion_point(class_scope:google.streetview.publish.v1.ListPhotosRequest)
  ))
_sym_db.RegisterMessage(ListPhotosRequest)

ListPhotosResponse = _reflection.GeneratedProtocolMessageType('ListPhotosResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTPHOTOSRESPONSE,
  __module__ = 'google.streetview.publish_v1.proto.rpcmessages_pb2'
  ,
  __doc__ = """Response to list all photos that belong to a user.
  
  
  Attributes:
      photos:
          List of photos. The [pageSize][google.streetview.publish.v1.Li
          stPhotosRequest.page\_size] field in the request determines
          the number of items returned.
      next_page_token:
          Token to retrieve the next page of results, or empty if there
          are no more results in the list.
  """,
  # @@protoc_insertion_point(class_scope:google.streetview.publish.v1.ListPhotosResponse)
  ))
_sym_db.RegisterMessage(ListPhotosResponse)

UpdatePhotoRequest = _reflection.GeneratedProtocolMessageType('UpdatePhotoRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEPHOTOREQUEST,
  __module__ = 'google.streetview.publish_v1.proto.rpcmessages_pb2'
  ,
  __doc__ = """Request to update the metadata of a
  [Photo][google.streetview.publish.v1.Photo]. Updating the pixels of a
  photo is not supported.
  
  
  Attributes:
      photo:
          Required. [Photo][google.streetview.publish.v1.Photo] object
          containing the new metadata.
      update_mask:
          Mask that identifies fields on the photo metadata to update.
          If not present, the old
          [Photo][google.streetview.publish.v1.Photo] metadata is
          entirely replaced with the new
          [Photo][google.streetview.publish.v1.Photo] metadata in this
          request. The update fails if invalid fields are specified.
          Multiple fields can be specified in a comma-delimited list.
          The following fields are valid:  -  ``pose.heading`` -
          ``pose.latLngPair`` -  ``pose.pitch`` -  ``pose.roll`` -
          ``pose.level`` -  ``pose.altitude`` -  ``connections`` -
          ``places``  .. raw:: html     <aside class="note">  Note: When
          [updateMask][google.streetview.publish.v1.UpdatePhotoRequest.u
          pdate\_mask] contains repeated fields, the entire set of
          repeated values get replaced with the new contents. For
          example, if [updateMask][google.streetview.publish.v1.UpdatePh
          otoRequest.update\_mask] contains ``connections`` and
          ``UpdatePhotoRequest.photo.connections`` is empty, all
          connections are removed.  .. raw:: html     </aside>
  """,
  # @@protoc_insertion_point(class_scope:google.streetview.publish.v1.UpdatePhotoRequest)
  ))
_sym_db.RegisterMessage(UpdatePhotoRequest)

BatchUpdatePhotosRequest = _reflection.GeneratedProtocolMessageType('BatchUpdatePhotosRequest', (_message.Message,), dict(
  DESCRIPTOR = _BATCHUPDATEPHOTOSREQUEST,
  __module__ = 'google.streetview.publish_v1.proto.rpcmessages_pb2'
  ,
  __doc__ = """Request to update the metadata of photos. Updating the pixels of photos
  is not supported.
  
  
  Attributes:
      update_photo_requests:
          Required. List of [UpdatePhotoRequests][google.streetview.publ
          ish.v1.UpdatePhotoRequest].
  """,
  # @@protoc_insertion_point(class_scope:google.streetview.publish.v1.BatchUpdatePhotosRequest)
  ))
_sym_db.RegisterMessage(BatchUpdatePhotosRequest)

BatchUpdatePhotosResponse = _reflection.GeneratedProtocolMessageType('BatchUpdatePhotosResponse', (_message.Message,), dict(
  DESCRIPTOR = _BATCHUPDATEPHOTOSRESPONSE,
  __module__ = 'google.streetview.publish_v1.proto.rpcmessages_pb2'
  ,
  __doc__ = """Response to batch update of metadata of one or more
  [Photos][google.streetview.publish.v1.Photo].
  
  
  Attributes:
      results:
          List of results for each individual
          [Photo][google.streetview.publish.v1.Photo] updated, in the
          same order as the request.
  """,
  # @@protoc_insertion_point(class_scope:google.streetview.publish.v1.BatchUpdatePhotosResponse)
  ))
_sym_db.RegisterMessage(BatchUpdatePhotosResponse)

DeletePhotoRequest = _reflection.GeneratedProtocolMessageType('DeletePhotoRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEPHOTOREQUEST,
  __module__ = 'google.streetview.publish_v1.proto.rpcmessages_pb2'
  ,
  __doc__ = """Request to delete a [Photo][google.streetview.publish.v1.Photo].
  
  
  Attributes:
      photo_id:
          Required. ID of the
          [Photo][google.streetview.publish.v1.Photo].
  """,
  # @@protoc_insertion_point(class_scope:google.streetview.publish.v1.DeletePhotoRequest)
  ))
_sym_db.RegisterMessage(DeletePhotoRequest)

BatchDeletePhotosRequest = _reflection.GeneratedProtocolMessageType('BatchDeletePhotosRequest', (_message.Message,), dict(
  DESCRIPTOR = _BATCHDELETEPHOTOSREQUEST,
  __module__ = 'google.streetview.publish_v1.proto.rpcmessages_pb2'
  ,
  __doc__ = """Request to delete multiple [Photos][google.streetview.publish.v1.Photo].
  
  
  Attributes:
      photo_ids:
          Required. IDs of the
          [Photos][google.streetview.publish.v1.Photo]. HTTP GET
          requests require the following syntax for the URL query
          parameter: ``photoIds=<id1>&photoIds=<id2>&...``.
  """,
  # @@protoc_insertion_point(class_scope:google.streetview.publish.v1.BatchDeletePhotosRequest)
  ))
_sym_db.RegisterMessage(BatchDeletePhotosRequest)

BatchDeletePhotosResponse = _reflection.GeneratedProtocolMessageType('BatchDeletePhotosResponse', (_message.Message,), dict(
  DESCRIPTOR = _BATCHDELETEPHOTOSRESPONSE,
  __module__ = 'google.streetview.publish_v1.proto.rpcmessages_pb2'
  ,
  __doc__ = """Response to batch delete of one or more
  [Photos][google.streetview.publish.v1.Photo].
  
  
  Attributes:
      status:
          The status for the operation to delete a single
          [Photo][google.streetview.publish.v1.Photo] in the batch
          request.
  """,
  # @@protoc_insertion_point(class_scope:google.streetview.publish.v1.BatchDeletePhotosResponse)
  ))
_sym_db.RegisterMessage(BatchDeletePhotosResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
