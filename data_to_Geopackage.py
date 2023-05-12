"""Read the NOAA HURDAT2 format

Documentation: https://www.nhc.noaa.gov/data/hurdat/hurdat2-format-atl-1851-2021.pdf
Source: https://www.nhc.noaa.gov/data/hurdat/hurdat2-1851-2021-100522.txt
"""

__author__ = "James Rapaport"
from os import environ

environ['PROJ_LIB'] =\
    'C:\\Users\\W0475475\\.conda\\envs\\prog5000\\Library\\share\\proj'

import csv
import datetime

import fiona
import fiona.crs


# Track shapefile schema
# this is a python dictionary i.e the schema
track_schema = {
    'geometry': 'LineString',
    'properties' : {
        'identifier' : 'str:8',
        # 'name': 'str:9',
        # 'year': 'int',
        # 'cyclone_no': 'int'
    }
}

# Observation schema
observation_schema = {
    'geometry': 'Point',
    'properties' : {
        'date_time' : 'datetime',
        'wind_speed': 'int',
        'pressure': 'int',
    }
}
# The track should have a CRS - we don't know what this is from the documentation ( I think
#  A reasonable
wgs84 = fiona.crs.from_epsg(4326)

with (open('D:\\python\\hurdat2-1851-2021-100522.txt', 'r') as hurdat,
        fiona.open('D:\\python\\hurdat.gpkg','w',
        driver= 'GPKG',
        schema=track_schema,
        crs=wgs84,
        layer='track')  as track,

        fiona.open('D:\\python\\hurdat.gpkg','w',
        driver= 'GPKG',
        schema=observation_schema,
        crs=wgs84,
        layer= 'observation')  as obs):
    # CSV reader
    reader = csv.reader(hurdat)
    # Read each row
    for row in reader:
        # The first row encountered is a header row
        # The first item on the row can be treated as an identifier
        # But the identifier also contains more information
        identifier = row[0]
        # The second item on the row is the hurricane name
        # It is padded with spaces. Use the lstrip() method of str
        # to remove the spaces
        name = row[1].lstrip()
        # The third item on the row is the number of data rows. The
        # item will be read as a string and we'll want to use it as
        # a number so cast it to an integer.
        data_rows = int(row[2].lstrip())
        # Now we're ready to read the data rows. The data_rows number
        # tells us how many to read... 
        # ******************************************************************************
        # We want to keep a list of points in the data section so that
        # a track can be be built as a line. Declare a dictionary here. This
        # will form a template of a GeoJSON geometry.
        # https://fiona.readthedocs.io/en/latest/manual.html#point-set-theory-and-simple-features
        # Python dictionary: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
        track_record = {
                "geometry": {
                    "type": "LineString", 
                    "coordinates": []
            },
            'properties':{
                'identifier': None
            }
        }


        # Writing one observation at a time seems
        # has a writerecords() function which might help speed things up. several records
        # be written in one transaction. Let's build a list of the observation records 
        # each hurricane and write them in one operation - on a per hurricane basis.

        observation_records = []

        for i in range(data_rows):
            # Get the next line
            # Python documentation https://docs.python.org/3/library/functions.html#next
            data_row = next(reader)

            #*******************************************************************
            # Observation record
            observation_record = {
                "geometry": {
                    "type": "Point", 
                    "coordinates": []
            },
            'properties':{
                'date_time': None,
                'wind_speed': None,
                'pressure': None
            }
        }
            # First item is the date
            date = data_row[0]
            # Next item is the time padded in HHMM format
            time = data_row[1].lstrip()
            # The date and time need to be parsed into python datetime object
            date_time = datetime.datetime.strptime(f'{date} {time}', '%Y%m%d %H%M')

            # Next is the record identifier which corresponds to a defined
            # list of letters which have meaning
            record_identifier = data_row[2].lstrip()
            # Status of the system
            status = data_row[3].lstrip()
            # Latitude - the value of latitude contains hemisphere (N/S)
            latitude = data_row[4].lstrip()
            # Longitude - the value of longitude contains hemisphere (E/W)
            longitude = data_row[5].lstrip()
            # Max sustained windspeed in knots. Looks like this should be 
            # an integer
            speed = int(data_row[6].lstrip())
            # Min pressure in millibars. Looks like this should be an
            # integer
            pressure = int(data_row[7].lstrip())
            # We're reading the points separately but we also want to be
            # able to form lines from the points...
            # We want to be able to use the latitude value as a number
            if 'N' in latitude:
                latitude = float(latitude.replace('N', ''))
            else:
                latitude = float(latitude.removesuffix('S')) * -1
            # We want to be able to use the longitude value as a number
            if 'E' in longitude:
                longitude = float(longitude.replace('E', ''))
            else:
                longitude = float(longitude.removesuffix('W')) * -1
            # Add the coordinates to the track
            track_record['geometry']['coordinates'].append((longitude, latitude))

            #************************************************************************************
            # Write the record for the observation
            observation_record['geometry']['coordinates'] = (longitude, latitude)
            observation_record['properties']['date_time'] = date_time
            observation_record['properties']['wind_speed'] = speed
            observation_record['properties']['pressure'] = pressure

            # Instead of writing the record here add it to the list of observation record
            observation_records.append(observation_record)

        # The nested for loop that processes the data rows is complete here so there 
        # should be a list of observations that can be written to the Geopackage file
        obs.writerecords(observation_records)

        # set the track property- its identifier
        track_record['properties']['identifier'] = identifier
        # Finally write the track record
        track.write(track_record)

            # ******************************************************************************
            # The coordinates must be stored in the record in order. Append them
            # to the coordinates list of the track_record. Note how the coordinates
            # list in the dictionary is accessed by its name. Previously we have accessed
            # items in a list using an index (ie by position).
            # Add the coordinates to the track
        track_record['geometry']['coordinates'].append((longitude, latitude))

        # Print the track
        print(track_record)



# Next we need to create the schema for the shapefile.
# Open a shapefile for writing.
# And write data.
# Let's start by writing just the identifier as an attribute.