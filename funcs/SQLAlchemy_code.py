import sqlalchemy
from sqlalchemy import create_engine
from config import host, user, password, db_name, port, num_of_tests
from sqlalchemy import URL
from sqlalchemy.sql import text
import statistics
import time

def SQLAlchemy_time():
    try:
        url_object = URL.create(
            "postgresql",
            username=user,
            password=password,
            host=host,
            database=db_name,
            port=port
        )

        engine = create_engine(url_object)
        con = engine.connect()

        # code
        results = []

        times = []
        statement = text("""
                                SELECT vendorid, count(*) FROM trips GROUP BY 1;
                                """)

        for i in range(num_of_tests):  # 1st question
            st_time = int(time.time_ns())
            con.execute(statement)
            end_time = int(time.time_ns())
            times.append(end_time - st_time)
        results.append(statistics.mean(times)/10**9)

        times = []
        statement = text("""
                                               SELECT passenger_count, avg(total_amount)
                                               FROM trips
                                               GROUP BY 1;
                                               """)
        for i in range(num_of_tests):  # 2nd question
            st_time = int(time.time_ns())
            con.execute(statement)
            end_time = int(time.time_ns())
            times.append(end_time - st_time)
        results.append(statistics.mean(times)/10**9)

        times = []
        statement = text("""
                                                SELECT
                                                passenger_count,
                                                extract(year from tpep_pickup_datetime),
                                                count(*)
                                                FROM trips
                                                GROUP BY 1, 2;
                                                """)
        for i in range(num_of_tests):  # 3rd question
            st_time = int(time.time_ns())
            con.execute(statement)
            end_time = int(time.time_ns())
            times.append(end_time - st_time)
        results.append(statistics.mean(times)/10**9)

        times = []
        statement = text("""
                                                SELECT
                                                passenger_count,
                                                extract(year from tpep_pickup_datetime),
                                                round(trip_distance),
                                                count(*)
                                                FROM trips
                                                GROUP BY 1, 2, 3
                                                ORDER BY 2, 4 desc;
                                                """)
        for i in range(num_of_tests):  # 4th question
            st_time = int(time.time_ns())
            con.execute(statement)
            end_time = int(time.time_ns())
            times.append(end_time - st_time)
        results.append(statistics.mean(times)/10**9)
        con.close()
        return results
    except create_engine.Error as e:
        print("ERROR in SQLAlchemy_code")
        print(e)
        return []