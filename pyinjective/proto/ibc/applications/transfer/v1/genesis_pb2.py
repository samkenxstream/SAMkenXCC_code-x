# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/transfer/v1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ibc.applications.transfer.v1 import transfer_pb2 as ibc_dot_applications_dot_transfer_dot_v1_dot_transfer__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*ibc/applications/transfer/v1/genesis.proto\x12\x1cibc.applications.transfer.v1\x1a+ibc/applications/transfer/v1/transfer.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\"\x90\x02\n\x0cGenesisState\x12\x0f\n\x07port_id\x18\x01 \x01(\t\x12N\n\x0c\x64\x65nom_traces\x18\x02 \x03(\x0b\x32(.ibc.applications.transfer.v1.DenomTraceB\x0e\xaa\xdf\x1f\x06Traces\xc8\xde\x1f\x00\x12:\n\x06params\x18\x03 \x01(\x0b\x32$.ibc.applications.transfer.v1.ParamsB\x04\xc8\xde\x1f\x00\x12\x63\n\x0etotal_escrowed\x18\x04 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xc8\xde\x1f\x00\x42\x39Z7github.com/cosmos/ibc-go/v7/modules/apps/transfer/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.transfer.v1.genesis_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z7github.com/cosmos/ibc-go/v7/modules/apps/transfer/types'
  _GENESISSTATE.fields_by_name['denom_traces']._options = None
  _GENESISSTATE.fields_by_name['denom_traces']._serialized_options = b'\252\337\037\006Traces\310\336\037\000'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['total_escrowed']._options = None
  _GENESISSTATE.fields_by_name['total_escrowed']._serialized_options = b'\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\310\336\037\000'
  _GENESISSTATE._serialized_start=176
  _GENESISSTATE._serialized_end=448
# @@protoc_insertion_point(module_scope)
