#sql_insert.py

import sqlite3 as lite

con = lite.connect("getting_started.db")

#Insert rows by passing values directly to execute function:

with con:
    cur = con.cursor()
    cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
    cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
    cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January',89)")
    cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January',94)")