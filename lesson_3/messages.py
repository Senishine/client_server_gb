from enum import Enum


class ServerResponseFieldName(Enum):
    RESPONSE = 'response'
    TIME = 'time'
    ALERT = 'alert'
    ERROR = 'error'


class MessageType(Enum):
    PRESENCE = 'presence'


class ResponseCode(Enum):
    OK = 200,
    BAD_REQUEST = 400
