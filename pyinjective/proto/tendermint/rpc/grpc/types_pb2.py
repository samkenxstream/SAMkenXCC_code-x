# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tendermint/rpc/grpc/types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tendermint.abci import types_pb2 as tendermint_dot_abci_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ftendermint/rpc/grpc/types.proto\x12\x13tendermint.rpc.grpc\x1a\x1btendermint/abci/types.proto\"\r\n\x0bRequestPing\" \n\x12RequestBroadcastTx\x12\n\n\x02tx\x18\x01 \x01(\x0c\"\x0e\n\x0cResponsePing\"\x81\x01\n\x13ResponseBroadcastTx\x12\x32\n\x08\x63heck_tx\x18\x01 \x01(\x0b\x32 .tendermint.abci.ResponseCheckTx\x12\x36\n\ndeliver_tx\x18\x02 \x01(\x0b\x32\".tendermint.abci.ResponseDeliverTx2\xbd\x01\n\x0c\x42roadcastAPI\x12K\n\x04Ping\x12 .tendermint.rpc.grpc.RequestPing\x1a!.tendermint.rpc.grpc.ResponsePing\x12`\n\x0b\x42roadcastTx\x12\'.tendermint.rpc.grpc.RequestBroadcastTx\x1a(.tendermint.rpc.grpc.ResponseBroadcastTxB4Z2github.com/tendermint/tendermint/rpc/grpc;coregrpcb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tendermint.rpc.grpc.types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/tendermint/tendermint/rpc/grpc;coregrpc'
  _REQUESTPING._serialized_start=85
  _REQUESTPING._serialized_end=98
  _REQUESTBROADCASTTX._serialized_start=100
  _REQUESTBROADCASTTX._serialized_end=132
  _RESPONSEPING._serialized_start=134
  _RESPONSEPING._serialized_end=148
  _RESPONSEBROADCASTTX._serialized_start=151
  _RESPONSEBROADCASTTX._serialized_end=280
  _BROADCASTAPI._serialized_start=283
  _BROADCASTAPI._serialized_end=472
# @@protoc_insertion_point(module_scope)
