#database.py

import sqlite3 as lite
import pandas as pd
import sys
import pdb

#INPUT DATA:
cities_tuple = (('New York City', 'NY'),
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA'))

weather_tuple = (("New York City",2013,"July","January",62),
    ("Boston",2013,"July","January",59),
    ("Chicago",2013,"July","January",59),
    ("Miami","2013","August","January",84),
    ("Dallas",2013,"July","January",77),
    ("Seattle",2013,"July","January",61),
    ("Portland",2013,"July","December",63),
    ("San Francisco",2013,"September","December",64),
    ("Los Angeles",2013,"September","December",75))

#FUNCTIONS:
def sql_functions(cities, weather):
    """Generate database, populate database and return input as dataframe."""
    con = lite.connect("sql_database.db")
    tables_tuple = ("cities", "weather")
    with con:
        #Generate tables in database:
        cur = con.cursor() #Get cursor object
        for table in tables_tuple:
            cur.execute("DROP TABLE IF EXISTS {0}".format(table)) #Drop tables if they already exist.
        cur.execute("CREATE TABLE cities (name text, state text)")
        cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer)")
        #Populate tables in database:
        cur.executemany("INSERT INTO cities VALUES (?,?)", cities)
        cur.executemany("INSERT INTO weather VALUES (?,?,?,?,?)", weather)
        #Retrieve data from database:
        cur.execute("SELECT * FROM cities INNER JOIN weather ON city = name")
        rows = cur.fetchall()
        cols = [desc[0] for desc in cur.description]
        output_dataframe = pd.DataFrame(rows, columns = cols)
    
    return output_dataframe

def check_user_input(input_dataframe):
    """Get command line input (CLI), check if CLI is present in warm_month/cold_month fields.
    Return CLI month if selection is present in database.
    Otherwise: exit program"""
    if len(sys.argv) >= 3:
        sys.exit("Too many command line inputs.  Use = python database.py <Month>")
    elif len(sys.argv) < 2:
        sys.exit("Use = python database.py <Month>")
    cli_month = str(sys.argv[1])
    #if cli_month not in input_dataframe["warm_month"].astype(str).tolist():
    if input_dataframe["warm_month"].str.contains(cli_month).any() == False: #Check if the data contains any warm month entries for CLI.
        sys.exit("The selected month \"{0}\" is not a warm month for any city in the database.".format(cli_month)) #If not, exit.
    
    return cli_month

def generate_output(cli_month, input_dataframe):
    "Print out cities which are hottest in the user selected month."
    is_hot = input_dataframe[input_dataframe["warm_month"] == cli_month] #Generate new dataframe for months which are equal to CLI.
    output_data_structure = is_hot[["city", "state"]].astype(str).values.tolist() #Generate list w/ structure 'city, state'
    output_list = [", ".join(i) for i in output_data_structure] #join nested list.
    output_string = ", ".join(output_list) #Generate output string. (Better to condense with prior line?)
    print "The hottest cities in {0} are: {1}.".format(cli_month, output_string) #Print to stdout.

#MAIN: 
def main():
    db_dataframe = sql_functions(cities_tuple, weather_tuple)
    cli_month = check_user_input(db_dataframe)
    generate_output(cli_month, db_dataframe)


if __name__ == "__main__":
    main()


