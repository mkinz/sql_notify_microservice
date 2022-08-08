from typing import Protocol, List
from dataclasses import dataclass


class IDataHolder(Protocol):
    ...


@dataclass
class DataHolder:
    sql_data: List[str]
