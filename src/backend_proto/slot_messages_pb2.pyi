from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSlotRequest(_message.Message):
    __slots__ = ["info", "user_id"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    info: SlotInfo
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., info: _Optional[_Union[SlotInfo, _Mapping]] = ...) -> None: ...

class CreateSlotResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateSlotsRequest(_message.Message):
    __slots__ = ["all", "each", "shelf_id", "slots", "user_id"]
    class PerSlotCapacity(_message.Message):
        __slots__ = ["capacity"]
        CAPACITY_FIELD_NUMBER: _ClassVar[int]
        capacity: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, capacity: _Optional[_Iterable[int]] = ...) -> None: ...
    ALL_FIELD_NUMBER: _ClassVar[int]
    EACH_FIELD_NUMBER: _ClassVar[int]
    SHELF_ID_FIELD_NUMBER: _ClassVar[int]
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    all: int
    each: CreateSlotsRequest.PerSlotCapacity
    shelf_id: str
    slots: int
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., shelf_id: _Optional[str] = ..., slots: _Optional[int] = ..., all: _Optional[int] = ..., each: _Optional[_Union[CreateSlotsRequest.PerSlotCapacity, _Mapping]] = ...) -> None: ...

class CreateSlotsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteSlotRequest(_message.Message):
    __slots__ = ["shelf_id", "slot_num", "user_id"]
    SHELF_ID_FIELD_NUMBER: _ClassVar[int]
    SLOT_NUM_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    shelf_id: str
    slot_num: int
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., shelf_id: _Optional[str] = ..., slot_num: _Optional[int] = ...) -> None: ...

class DeleteSlotResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ReadSlotRequest(_message.Message):
    __slots__ = ["shelf_id", "slot_num", "user_id"]
    SHELF_ID_FIELD_NUMBER: _ClassVar[int]
    SLOT_NUM_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    shelf_id: str
    slot_num: int
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., shelf_id: _Optional[str] = ..., slot_num: _Optional[int] = ...) -> None: ...

class ReadSlotResponse(_message.Message):
    __slots__ = ["info"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: SlotInfo
    def __init__(self, info: _Optional[_Union[SlotInfo, _Mapping]] = ...) -> None: ...

class SlotInfo(_message.Message):
    __slots__ = ["capacity", "item_count", "slot_num"]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    SLOT_NUM_FIELD_NUMBER: _ClassVar[int]
    capacity: int
    item_count: int
    slot_num: int
    def __init__(self, slot_num: _Optional[int] = ..., capacity: _Optional[int] = ..., item_count: _Optional[int] = ...) -> None: ...

class UpdateSlotRequest(_message.Message):
    __slots__ = ["new_info", "shelf_id", "slot_num", "user_id"]
    NEW_INFO_FIELD_NUMBER: _ClassVar[int]
    SHELF_ID_FIELD_NUMBER: _ClassVar[int]
    SLOT_NUM_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    new_info: SlotInfo
    shelf_id: str
    slot_num: int
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., shelf_id: _Optional[str] = ..., slot_num: _Optional[int] = ..., new_info: _Optional[_Union[SlotInfo, _Mapping]] = ...) -> None: ...

class UpdateSlotResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
