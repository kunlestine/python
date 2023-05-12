""" Connect to a PostgreSQL database"""

import psycopg2


# connect to an existing database. The connect method is a constructor
# for a Connection object
connection = psycopg2.connect('dbname=assignment3 user=postgres password=postgres')

# A connection provides a database cursor represented by
# the cursor object. A cursor is used to execute sql. It provides
# a means to frtch rows from the database and to interact with them.
# using the cursor() method
cursor = connection.cursor()

# Print PostgreSQL details
# print("PostgreSQL server information")
# print(connection.get_dsn_parameters(), "\n")

# Use the execute method of a cursor to execute the query
# The cursor will execute SQL
with connection:
    cursor.execute("CREATE TABLE bathymetry.ocean(identifier serial PRIMARY KEY, name varchar(16));")

    # Pass data to fill aquery placeholders and let Psycopg perform
    # the correct conversion (no more SQL injections!)

    cursor.execute("""INSERT INTO bathymetry.ocean(identifier, name) 
                    VALUES (%s, %s);""",
                  (1, "North Sea", ))


# cursor.execute("SELECT * FROM asset.ocean;")
# print(cursor.fetchall())

# with connection:
#     cursor.execute("CREATE TABLE bathymetry.location(l_identifier serial PRIMARY KEY, location varchar(50));")

#     # Pass data to fill aquery placeholders and let Psycopg perform
#     # the correct conversion (no more SQL injections!)

#     cursor.execute("""INSERT INTO bathymetry.location(l_identifier, location) 
#                     VALUES (%s, %s);""",
#                   (1, "Bridlington Bay", ))
#     cursor.execute("""INSERT INTO bathymetry.location(l_identifier, location) 
#                     VALUES (%s, %s);""",
#                   (2,"Flamborough Head Ground", ))
#     cursor.execute("""INSERT INTO bathymetry.location(l_identifier, location) 
#                     VALUES (%s, %s);""",
#                   (3, "Whitby Ground to Flamborough Head Ground", ))
#     cursor.execute("""INSERT INTO bathymetry.location(l_identifier, location) 
#                     VALUES (%s, %s);""",
#                   (4, "Outer Silver Pit", ))
#     cursor.execute("""INSERT INTO bathymetry.location(l_identifier, location) 
#                     VALUES (%s, %s);""",
#                   (5,"Spurn Head to Flamborough Head", ))


# cursor.execute("SELECT * FROM asset.ocean;")
# print(cursor.fetchall())

