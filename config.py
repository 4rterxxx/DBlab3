# Имя файла с таблицей

name_of_file = "data_wo_unnamed.csv"

# data for postgres, pandas, sqlalchemy

host = "localhost"
user = "postgres"
password = "postgres"
db_name = "postgres"
port = 5432

# data for SQLite3

name_of_file_db = "sqlite.db" # Указать адрес файла с бд в формате .db или .sql/ При отсутствии такого файла оставить пустым (файл создастся из автоматически .csv с именем sqlite.db)

# Количество тестов

num_of_tests = 10

# Какие библиотеки сравниваем

isPostgre = True
isSQLite = True
isDuckDB = True
isPandas = True
isSQLAlchemy = True

# True - идёт в сравнение, False - не идёт
