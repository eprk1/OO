from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto


class Device(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

class DeviceProtocol(Protocol):
    def connect(self) -> None:
        ...

class MessageType(Enum):
    SWITCH_ON = auto()

@dataclass
class Message:
    device_id: str
    msg_type = MessageType
    data: str = ""


class Curtains(Device):
    def connect(self) -> None:
        print("Connecting to Curtains")

class HueLight:
    def connect(self) -> None:
        print("Connecting to Hue light.")
