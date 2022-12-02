# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: frontend_proto/frontend_messages.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&frontend_proto/frontend_messages.proto\x12\x11sims_ims_frontend\"2\n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x16\n\x05Token\x12\r\n\x05token\x18\x01 \x01(\t\"V\n\x0c\x43lientAction\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\t\x12%\n\x04info\x18\x03 \x01(\x0b\x32\x17.sims_ims_frontend.Info\"\x10\n\x0e\x41\x63tionApproved\"=\n\x08ItemInfo\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\r\x12\r\n\x05stock\x18\x03 \x01(\r\"2\n\tShelfInfo\x12\x10\n\x08shelf_id\x18\x01 \x01(\t\x12\x13\n\x0bshelf_count\x18\x02 \x01(\r\"B\n\x08SlotInfo\x12\x10\n\x08slot_num\x18\x01 \x01(\r\x12\x10\n\x08\x63\x61pacity\x18\x02 \x01(\r\x12\x12\n\nitem_count\x18\x03 \x01(\r\"\x95\x01\n\x04Info\x12/\n\tshelfInfo\x18\x01 \x01(\x0b\x32\x1c.sims_ims_frontend.ShelfInfo\x12-\n\x08itemInfo\x18\x02 \x01(\x0b\x32\x1b.sims_ims_frontend.ItemInfo\x12-\n\x08slotInfo\x18\x03 \x01(\x0b\x32\x1b.sims_ims_frontend.SlotInfo\"X\n\x11GetShelvesRequest\x12\x15\n\x08shelf_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05token\x18\x03 \x01(\tB\x0b\n\t_shelf_id\"U\n\x0eGetSlotRequest\x12\x15\n\x08slot_num\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05token\x18\x03 \x01(\tB\x0b\n\t_slot_num\"{\n\x0eGetItemRequest\x12\x16\n\tobject_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08shelf_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x10\n\x08username\x18\x03 \x01(\t\x12\r\n\x05token\x18\x04 \x01(\tB\x0c\n\n_object_idB\x0b\n\t_shelf_id\"3\n\x05Items\x12*\n\x05items\x18\x01 \x03(\x0b\x32\x1b.sims_ims_frontend.ItemInfo\"3\n\x05Slots\x12*\n\x05slots\x18\x01 \x03(\x0b\x32\x1b.sims_ims_frontend.SlotInfo\"8\n\x07Shelves\x12-\n\x07shelves\x18\x01 \x03(\x0b\x32\x1c.sims_ims_frontend.ShelfInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'frontend_proto.frontend_messages_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOGINREQUEST._serialized_start=61
  _LOGINREQUEST._serialized_end=111
  _TOKEN._serialized_start=113
  _TOKEN._serialized_end=135
  _CLIENTACTION._serialized_start=137
  _CLIENTACTION._serialized_end=223
  _ACTIONAPPROVED._serialized_start=225
  _ACTIONAPPROVED._serialized_end=241
  _ITEMINFO._serialized_start=243
  _ITEMINFO._serialized_end=304
  _SHELFINFO._serialized_start=306
  _SHELFINFO._serialized_end=356
  _SLOTINFO._serialized_start=358
  _SLOTINFO._serialized_end=424
  _INFO._serialized_start=427
  _INFO._serialized_end=576
  _GETSHELVESREQUEST._serialized_start=578
  _GETSHELVESREQUEST._serialized_end=666
  _GETSLOTREQUEST._serialized_start=668
  _GETSLOTREQUEST._serialized_end=753
  _GETITEMREQUEST._serialized_start=755
  _GETITEMREQUEST._serialized_end=878
  _ITEMS._serialized_start=880
  _ITEMS._serialized_end=931
  _SLOTS._serialized_start=933
  _SLOTS._serialized_end=984
  _SHELVES._serialized_start=986
  _SHELVES._serialized_end=1042
# @@protoc_insertion_point(module_scope)
