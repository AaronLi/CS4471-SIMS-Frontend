from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateShelfRequest(_message.Message):
    __slots__ = ["info", "user_id"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    info: ShelfInfo
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., info: _Optional[_Union[ShelfInfo, _Mapping]] = ...) -> None: ...

class CreateShelfResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteShelfRequest(_message.Message):
    __slots__ = ["target", "user_id"]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    target: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., target: _Optional[str] = ...) -> None: ...

class DeleteShelfResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ReadShelfRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class ReadShelfResponse(_message.Message):
    __slots__ = ["info"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: _containers.RepeatedCompositeFieldContainer[ShelfInfo]
    def __init__(self, info: _Optional[_Iterable[_Union[ShelfInfo, _Mapping]]] = ...) -> None: ...

class ShelfInfo(_message.Message):
    __slots__ = ["shelf_count", "shelf_id"]
    SHELF_COUNT_FIELD_NUMBER: _ClassVar[int]
    SHELF_ID_FIELD_NUMBER: _ClassVar[int]
    shelf_count: int
    shelf_id: str
    def __init__(self, shelf_id: _Optional[str] = ..., shelf_count: _Optional[int] = ...) -> None: ...

class UpdateShelfRequest(_message.Message):
    __slots__ = ["new_state", "target", "user_id"]
    NEW_STATE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    new_state: ShelfInfo
    target: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., target: _Optional[str] = ..., new_state: _Optional[_Union[ShelfInfo, _Mapping]] = ...) -> None: ...

class UpdateShelfResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
