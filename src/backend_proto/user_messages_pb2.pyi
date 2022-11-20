from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateUserRequest(_message.Message):
    __slots__ = ["info"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: UserInfo
    def __init__(self, info: _Optional[_Union[UserInfo, _Mapping]] = ...) -> None: ...

class CreateUserResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteUserRequest(_message.Message):
    __slots__ = ["info"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: UserInfo
    def __init__(self, info: _Optional[_Union[UserInfo, _Mapping]] = ...) -> None: ...

class DeleteUserResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ReadUserRequest(_message.Message):
    __slots__ = ["info"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: UserInfo
    def __init__(self, info: _Optional[_Union[UserInfo, _Mapping]] = ...) -> None: ...

class ReadUserResponse(_message.Message):
    __slots__ = ["info"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: UserInfo
    def __init__(self, info: _Optional[_Union[UserInfo, _Mapping]] = ...) -> None: ...

class UserInfo(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...
