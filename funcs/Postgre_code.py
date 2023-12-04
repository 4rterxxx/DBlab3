import psycopg2
from config import host, user, password, db_name, port, num_of_tests
import time
import statistics

def Postgre_time():
        try:
                conn = psycopg2.connect(
                        host=host,
                        user=user,
                        password=password,
                        database=db_name,
                        port=port
                )

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
                                                extract(year from tpep_pickup_datetime),
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
                                                extract(year from tpep_pickup_datetime),
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

                # print(cur.fetchall())
                conn.commit()
                cur.close()
                conn.close()
                return results
        except psycopg2.Error as e:
                print("ERROR in Postgre_code")
                print(e)
                return []