from dataholder import DataHolder


def test_dataholder():
    tmp_list = []
    dut = DataHolder(tmp_list)
    assert isinstance(dut.sql_data, list)
    dut.sql_data.append("0")
    assert dut.sql_data[0] == "0"

def test_dataholder_calculates_hash_of_stored_data():
    tmplist = ['1', '2', '3']
    dut = DataHolder(tmplist)
    hashval = hash(str(''.join(tmplist)))
    assert dut.get_hash_of_sql_data() == hashval
