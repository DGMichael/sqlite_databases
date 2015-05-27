#sql_exemany.property

import sqlite3 as lite

#Example tuples to pass:
cities = (("Las Vegas", "NV"), ("Atlanta", "GA"))
weather = (("Las Vegas", 2013, "July", "December", 101), ("Atlanta", 2013, "July", "January", 99))

con = lite.connect("getting_started.db")
#Insert rows by passing tuples to execute()
with con:
    cur = con.cursor()
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
