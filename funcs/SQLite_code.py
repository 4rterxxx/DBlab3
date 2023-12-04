import sqlite3
import pandas as pd
from config import name_of_file, num_of_tests, name_of_file_db
import time
import statistics

def SQLite_time():
    try:
        if (name_of_file_db == ""):
            table = pd.read_csv(name_of_file)
            table.columns = table.columns.str.strip()
            table['tpep_pickup_datetime'] = pd.to_datetime(table['tpep_pickup_datetime'])
            table['tpep_dropoff_datetime'] = pd.to_datetime(table['tpep_dropoff_datetime'])
            conn = sqlite3.connect("sqlite.db")
            table.to_sql("trips", conn, if_exists="replace")
            conn.commit()
            conn.close()
            conn = sqlite3.connect("sqlite.db")
        else:
            conn = sqlite3.connect(name_of_file_db)

        cur = conn.cursor()

        # code here

        results = []

        times = []
        for i in range(num_of_tests):  # 1st question
            st_time = int(time.time_ns())
            cur.execute("""
                                SELECT vendorid, count(*) FROM trips GROUP BY 1;
                                """)
            end_time = int(time.time_ns())
            times.append(end_time - st_time)
        results.append(statistics.mean(times)/10**9)

        times = []
        for i in range(num_of_tests):  # 2nd question
            st_time = int(time.time_ns())
            cur.execute("""
                                               SELECT passenger_count, avg(total_amount)
                                               FROM trips
                                               GROUP BY 1;
                                               """)
            end_time = int(time.time_ns())
            times.append(end_time - st_time)
        results.append(statistics.mean(times)/10**9)

        times = []
        for i in range(num_of_tests):  # 3rd question
            st_time = int(time.time_ns())
            cur.execute("""
            SELECT
            passenger_count,
            strftime('%Y', tpep_pickup_datetime),
            count(*)
            FROM trips
            GROUP BY 1, 2;
            """)
            end_time = int(time.time_ns())
            times.append(end_time - st_time)
        results.append(statistics.mean(times)/10**9)

        times = []
        for i in range(num_of_tests):  # 4th question
            st_time = int(time.time_ns())
            cur.execute(""" 
            SELECT
                                        passenger_count,
                                        strftime('%Y', tpep_pickup_datetime),
                                        round(trip_distance),
                                        count(*)
                                        FROM trips
                                        GROUP BY 1, 2, 3
                                        ORDER BY 2, 4 desc;
            """)
            end_time = int(time.time_ns())
            times.append(end_time - st_time)
        results.append(statistics.mean(times)/10**9)

        # end code

        conn.commit()
        cur.close()
        conn.close()
        return results


    except sqlite3.Error as e:
        print("ERROR in SQLite_code")
        print(e)
        return []
