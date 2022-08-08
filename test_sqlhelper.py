from sqlhelper import GenericSQLHelper


def test_initialize_sql_helper():
    dut = GenericSQLHelper()
    assert dut.connection.connected is False
    dut.connection.connect_do_database()
    assert dut.connection.connected is True
