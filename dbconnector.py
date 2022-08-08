from typing import Protocol
from dataclasses import dataclass


class IDBConnector(Protocol):
    ...


@dataclass
class DBConnector:
    username: str = "test_user"
    password: str = "test_password"
    connection_str: str = "mock_db_connection"
    connected: bool = False

    def connect_do_database(self, *args):
        self.connected = True
        return f"Connected to database {self.connection_str}"


