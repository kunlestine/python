from os import environ

environ['PROJ_LIB'] = 'C:\\Users\\W0475475\\.conda\\envs\\prog5000\\Library\\share\\proj'
import rasterio
import fiona
import shapely.geometry
import shapely.ops
import shapely.wkb
import pyproj
import psycopg2


""" Connect to a PostgreSQL database"""
epsg3348 = pyproj.CRS.from_epsg(3348)

# connect to an existing database. The connect method is a constructor
# for a Connection object
connection = psycopg2.connect('dbname=assignment1 user=postgres password=postgres')

# A connection provides a database cursor represented by
# the cursor object. A cursor is used to execute sql. It provides
# a means to frtch rows from the database and to interact with them.
# using the cursor() method
cursor = connection.cursor()

# Use the execute method of a cursor to execute the query
# The cursor will execute SQL
sql = """select cd.cduid, cd.cdname,cd.cdboundary, cd.aeboundary
         from geography.census_division cd"""
   
cursor.execute(sql)
# opening  the gebco data

with (rasterio.open('D:\\python\\week 10\\gebco_2022_sub_ice_n90.0_s0.0_w-90.0_e0.0_subset.tif', 'r') as aq):
    # Fetch each record in turn from the cursor
    for record in cursor.fetchall(): # r is the records that contains a number of columns
         ns_geom = shapely.wkb.loads(record[2], hex=True)
         count = 0

