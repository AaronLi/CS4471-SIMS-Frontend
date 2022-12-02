from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionApproved(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ClientAction(_message.Message):
    __slots__ = ["action", "info", "user_id"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    action: str
    info: Info
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., action: _Optional[str] = ..., info: _Optional[_Union[Info, _Mapping]] = ...) -> None: ...

class Info(_message.Message):
    __slots__ = ["itemInfo", "shelfInfo", "slotInfo"]
    ITEMINFO_FIELD_NUMBER: _ClassVar[int]
    SHELFINFO_FIELD_NUMBER: _ClassVar[int]
    SLOTINFO_FIELD_NUMBER: _ClassVar[int]
    itemInfo: ItemInfo
    shelfInfo: ShelfInfo
    slotInfo: SlotInfo
    def __init__(self, shelfInfo: _Optional[_Union[ShelfInfo, _Mapping]] = ..., itemInfo: _Optional[_Union[ItemInfo, _Mapping]] = ..., slotInfo: _Optional[_Union[SlotInfo, _Mapping]] = ...) -> None: ...

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

class LoginRequest(_message.Message):
    __slots__ = ["password", "username"]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    password: str
    username: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class ShelfInfo(_message.Message):
    __slots__ = ["shelf_count", "shelf_id"]
    SHELF_COUNT_FIELD_NUMBER: _ClassVar[int]
    SHELF_ID_FIELD_NUMBER: _ClassVar[int]
    shelf_count: int
    shelf_id: str
    def __init__(self, shelf_id: _Optional[str] = ..., shelf_count: _Optional[int] = ...) -> None: ...

class SlotInfo(_message.Message):
    __slots__ = ["capacity", "item_count", "slot_num"]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    SLOT_NUM_FIELD_NUMBER: _ClassVar[int]
    capacity: int
    item_count: int
    slot_num: int
    def __init__(self, slot_num: _Optional[int] = ..., capacity: _Optional[int] = ..., item_count: _Optional[int] = ...) -> None: ...

class Token(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...
