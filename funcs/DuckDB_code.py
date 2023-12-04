import duckdb
from config import name_of_file, num_of_tests
import time
import statistics


def DuckDB_time():
    try:
        conn = duckdb.connect()

        # code here

        results = []

        times = []
        for i in range(num_of_tests):  # 1st question
            st_time = int(time.time_ns())
            conn.execute(f"""SELECT vendorid, count(*) FROM {name_of_file} GROUP BY 1;""")
            end_time = int(time.time_ns())
            times.append(end_time - st_time)
        results.append(statistics.mean(times)/10**9)

        times = []
        for i in range(num_of_tests):  # 2nd question
            st_time = int(time.time_ns())
            conn.execute(f"""
            SELECT passenger_count, avg(total_amount)
            FROM {name_of_file}
            GROUP BY 1;
            """)
            end_time = int(time.time_ns())
            times.append(end_time - st_time)
        results.append(statistics.mean(times)/10**9)

        times = []
        for i in range(num_of_tests):  # 3rd question
            st_time = int(time.time_ns())
            conn.execute(f"""
            SELECT
            passenger_count,
            extract(year from tpep_pickup_datetime),
            count(*)
            FROM {name_of_file}
            GROUP BY 1, 2;
            """)
            end_time = int(time.time_ns())
            times.append(end_time - st_time)
        results.append(statistics.mean(times)/10**9)

        times = []
        for i in range(num_of_tests):  # 4th question
            st_time = int(time.time_ns())
            conn.execute(f"""
            SELECT
            passenger_count,
            extract(year from tpep_pickup_datetime),
            round(trip_distance),
            count(*)
            FROM {name_of_file}
            GROUP BY 1, 2, 3
            ORDER BY 2, 4 desc;
            """)
            end_time = int(time.time_ns())
            times.append(end_time - st_time)
        results.append(statistics.mean(times)/10**9)

        # end code

        conn.close()
        return results
    except duckdb.Error as e:
        print("ERROR in DuckDB_code")
        print(e)
        return []