import matplotlib.pyplot as plt
from funcs.Postgre_code import Postgre_time
from funcs.SQLite_code import SQLite_time
from funcs.DuckDB_code import DuckDB_time
from funcs.Pandas_code import Pandas_time
from funcs.SQLAlchemy_code import SQLAlchemy_time
from config import isPostgre, isSQLite, isSQLAlchemy, isPandas, isDuckDB
import numpy as np

plt.title('Результаты бенчмарка')
width = 0.1
plt.grid()
x = [0,1,2,3]
x_indexes = np.arange(len(x))
plt.xticks(x, ['Q1', 'Q2', 'Q3', 'Q4'])
print("Results of benchmark:")
if (isPostgre):
    y1 = Postgre_time()
    print("Postgre ", *y1)
    if len(y1) != 0:
        plt.bar(x_indexes-(width*2), y1, label="Postgre", width=width)


if (isSQLite):
    y2 = SQLite_time()
    print("SQLite ", *y2)
    if len(y2)!=0:
        plt.bar(x_indexes- (width), y2, label="SQLite", width=width)

if (isDuckDB):
    y3 = DuckDB_time()
    print("DuckDB ", *y3)
    if len(y3) != 0:
        plt.bar(x_indexes, y3, label="DuckDB", width=width)

if (isPandas):
    y4 = Pandas_time()
    print("Pandas ", *y4)
    if len(y4) != 0:
        plt.bar(x_indexes + width, y4, label="Pandas", width=width)

if (isSQLAlchemy):
    y5 = SQLAlchemy_time()
    print("SQLAlchemy ", *y5)
    if len(y5) != 0:
        plt.bar(x_indexes + (2*width), y5, label="SQLAlchemy", width=width)

plt.legend()
plt.show()