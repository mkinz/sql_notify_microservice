from typing import Protocol
from dataclasses import dataclass


class IDataHolder(Protocol):
    ...


@dataclass
class DataHolder:
    pass
