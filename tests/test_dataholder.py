from dataholder import DataHolder


def test_dataholder():
    tmp_list = []
    dut = DataHolder(tmp_list)
    assert isinstance(dut.sql_data, list)
    dut.sql_data.append("0")
    assert dut.sql_data[0] == "0"
