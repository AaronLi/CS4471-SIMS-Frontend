from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateItemRequest(_message.Message):
    __slots__ = ["info", "shelf_id", "slot_number", "user_id"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    SHELF_ID_FIELD_NUMBER: _ClassVar[int]
    SLOT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    info: ItemInfo
    shelf_id: str
    slot_number: int
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., shelf_id: _Optional[str] = ..., slot_number: _Optional[int] = ..., info: _Optional[_Union[ItemInfo, _Mapping]] = ...) -> None: ...

class CreateItemResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteItemRequest(_message.Message):
    __slots__ = ["item_id", "user_id"]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    item_id: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., item_id: _Optional[str] = ...) -> None: ...

class DeleteItemResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ItemInfo(_message.Message):
    __slots__ = ["description", "object_id", "price", "stock"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    STOCK_FIELD_NUMBER: _ClassVar[int]
    description: str
    object_id: int
    price: int
    stock: int
    def __init__(self, description: _Optional[str] = ..., object_id: _Optional[int] = ..., price: _Optional[int] = ..., stock: _Optional[int] = ...) -> None: ...

class ReadItemRequest(_message.Message):
    __slots__ = ["item_id", "user_id"]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    item_id: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., item_id: _Optional[str] = ...) -> None: ...

class ReadItemResponse(_message.Message):
    __slots__ = ["info"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: ItemInfo
    def __init__(self, info: _Optional[_Union[ItemInfo, _Mapping]] = ...) -> None: ...

class UpdateItemRequest(_message.Message):
    __slots__ = ["item_id", "new_info", "user_id"]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_INFO_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    item_id: str
    new_info: ItemInfo
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., item_id: _Optional[str] = ..., new_info: _Optional[_Union[ItemInfo, _Mapping]] = ...) -> None: ...

class UpdateItemResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
