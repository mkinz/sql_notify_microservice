from sqlhelper import GenericSQLHelper

class Runner:
    def run_it(self):
        worker_bee = GenericSQLHelper()
        schema = "test_schema"
        table = "test_table"
        data_to_load = worker_bee.execute_sql(schema, table)
        worker_bee.write_sql_to_data_holder(data_to_load)

        if worker_bee.data_holder.get_hash_of_sql_data() != 0:
            print(f"Subject: New Data Found for date: {worker_bee.dth.today}")
            print("The following new data was found:")
            print(f"{worker_bee.data_holder.sql_data}")
        else:
            pass


runner = Runner()
runner.run_it()