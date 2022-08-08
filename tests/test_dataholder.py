from dataholder import DataHolder

def test_dataholder():
    tmp_list = []
    dut = DataHolder(tmp_list)
    assert isinstance(dut.sql_data, list)
