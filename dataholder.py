from typing import Protocol, List, Optional
from dataclasses import dataclass


class IDataHolder(Protocol):
    ...


@dataclass
class DataHolder:
    sql_data: Optional[List[str]]
