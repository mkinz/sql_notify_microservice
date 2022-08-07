from dbconnector import DBConnector


def test_db_connector_default_args():
    dut = DBConnector()
    assert dut.username == "test_user"
    assert dut.password == "test_password"


def test_connection_method_on_object_with_keyword_overrides():
    username = "matt"
    password = "password"
    connection_str = "testtest"
    dut = DBConnector(username, password, connection_str)
    assert dut.username == "matt"
    assert dut.password == "password"
    assert dut.connection_str == "testtest"


def test_connection_method_on_object():
    dut = DBConnector()
    dut.connect_do_database()
    assert dut.connected is True
