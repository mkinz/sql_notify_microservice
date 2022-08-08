from pandas import DataFrame, read_sql
from typing import Protocol
from dbconnector import DBConnector


class ISQLHelper(Protocol):
    ...


class GenericSQLHelper:

    def __init__(self):
        self.connection = DBConnector()

    @property
    def dbcon(self):
        return self.connection

    @dbcon.setter
    def dbcon(self, value):
        self.connection = value

    def execute_sql(self, schema: str, table: str) -> DataFrame:
        conn = self.connection.connection_str
        query = f"""
        select *
        from {schema}.{table}
        limit 5
        """
        return read_sql(query, conn)
