# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/framework/graph.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.framework import node_def_pb2 as tensorflow_dot_core_dot_framework_dot_node__def__pb2
from tensorflow.core.framework import function_pb2 as tensorflow_dot_core_dot_framework_dot_function__pb2
from tensorflow.core.framework import versions_pb2 as tensorflow_dot_core_dot_framework_dot_versions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/framework/graph.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_pb=_b('\n%tensorflow/core/framework/graph.proto\x12\ntensorflow\x1a(tensorflow/core/framework/node_def.proto\x1a(tensorflow/core/framework/function.proto\x1a(tensorflow/core/framework/versions.proto\"\x9d\x01\n\x08GraphDef\x12!\n\x04node\x18\x01 \x03(\x0b\x32\x13.tensorflow.NodeDef\x12(\n\x08versions\x18\x04 \x01(\x0b\x32\x16.tensorflow.VersionDef\x12\x13\n\x07version\x18\x03 \x01(\x05\x42\x02\x18\x01\x12/\n\x07library\x18\x02 \x01(\x0b\x32\x1e.tensorflow.FunctionDefLibraryBk\n\x18org.tensorflow.frameworkB\x0bGraphProtosP\x01Z=github.com/tensorflow/tensorflow/tensorflow/go/core/framework\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[tensorflow_dot_core_dot_framework_dot_node__def__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_function__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_versions__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GRAPHDEF = _descriptor.Descriptor(
  name='GraphDef',
  full_name='tensorflow.GraphDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='tensorflow.GraphDef.node', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='versions', full_name='tensorflow.GraphDef.versions', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='tensorflow.GraphDef.version', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
    _descriptor.FieldDescriptor(
      name='library', full_name='tensorflow.GraphDef.library', index=3,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=180,
  serialized_end=337,
)

_GRAPHDEF.fields_by_name['node'].message_type = tensorflow_dot_core_dot_framework_dot_node__def__pb2._NODEDEF
_GRAPHDEF.fields_by_name['versions'].message_type = tensorflow_dot_core_dot_framework_dot_versions__pb2._VERSIONDEF
_GRAPHDEF.fields_by_name['library'].message_type = tensorflow_dot_core_dot_framework_dot_function__pb2._FUNCTIONDEFLIBRARY
DESCRIPTOR.message_types_by_name['GraphDef'] = _GRAPHDEF

GraphDef = _reflection.GeneratedProtocolMessageType('GraphDef', (_message.Message,), dict(
  DESCRIPTOR = _GRAPHDEF,
  __module__ = 'tensorflow.core.framework.graph_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.GraphDef)
  ))
_sym_db.RegisterMessage(GraphDef)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030org.tensorflow.frameworkB\013GraphProtosP\001Z=github.com/tensorflow/tensorflow/tensorflow/go/core/framework\370\001\001'))
_GRAPHDEF.fields_by_name['version'].has_options = True
_GRAPHDEF.fields_by_name['version']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
# @@protoc_insertion_point(module_scope)
