import sqlite3 as lite

#connect to database, connection method returns a connection object
con = lite.connect("getting_started.db")

with con:
    #From connection, get a cursor object, cursor goes over the records returned from a query
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    #Fetching one record from cursor object
    data = cur.fetchone()
    #print result
    print "SQLite version = {data}".format(data = data)
    print data
