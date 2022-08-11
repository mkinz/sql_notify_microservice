from typing import Protocol, List, Optional
from dataclasses import dataclass


class IDataHolder(Protocol):
    ...


@dataclass
class DataHolder:
    sql_data: Optional[List[str]]

    def get_hash_of_sql_data(self):
        return hash(str(''.join(self.sql_data)))

    def print_contents_of_dataholder(self):
        for item in self.sql_data:
            print(item)
