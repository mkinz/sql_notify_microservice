from pandas import DataFrame, read_sql
from typing import Protocol
from dbconnector import DBConnector
from datetimehelper import DateTimeHelper
from dataholder import DataHolder


class ISQLHelper(Protocol):

    def execute_sql(self, schema: str, table: str) -> str:
        ...

    def write_sql_to_data_holder(self, query_data):
        ...


class GenericSQLHelper:

    def __init__(self):
        self.connection = DBConnector()
        self.dth = DateTimeHelper()
        self.data_holder = DataHolder([])

    @property
    def dbcon(self):
        return self.connection

    @dbcon.setter
    def dbcon(self, value):
        self.connection = value

    def execute_sql(self, schema: str, table: str) -> str:
        conn = self.connection.connection_str
        query = f"select * from {schema}.{table} where date == {self.dth.today} limit 5"
        # returned_data = read_sql(query, conn)
        returned_data = f"MOCKED_RETURN_DATA"
        return returned_data

    def write_sql_to_data_holder(self, query_data):
        self.data_holder.sql_data.append(query_data)
