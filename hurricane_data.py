__author__ = " Adeoya Adekunle"

import csv

with open('D:\\python\\hurdat2-1851-2021-100522.txt', 'r') as hurdat:
    # CSV reader
    reader = csv.reader(hurdat)
    # REad each row
    for row in reader:
        # The first row encountered is a header row
        # The first item on the row can be treated as an identifier
        #  But the identifier also contains more information
        identifier = row[0] 
        # The second item on the row is the hurricane name
        # It is padded with spaces. Use the lstrip() method of str
        # to remove the spaces
        """The lstrip() method returns a copy of the string with leading characters removed 
        (based on the string argument passed). 
        The lstrip() removes characters from the left based on the argument 
        (a string specifying the set of characters to be removed)."""
        name = row[1].lstrip()
        # THe third item on the row is the number of data rows. The
        # item will be read as a string and we'll want to use it as
         # a number so cast it to an integer.
        data_rows = int(row[2].lstrip())
        # Now we're ready to read the data rows. The data_rows number
        # tells us how many to read...
        #*************************************************************
        # We want to keep a list of points in the data section so that
        # a track can be built as a line. Declare a dictionary here. Tis
        # will form a template of a GeoJSON geometry.

        track_record = {
                "geometry": {
                    "type": "Linestring",
                    "coordinates": []
                }
        }
        for i in range(data_rows):
            # Get the next line 
            # Python documentation https://docs.python.org/3/library/functions.html#next
            data_row = next(reader)
            # First item is the date
            date = data_row[0]
            # Next item is the time padded in HHMM format

            print(data_row)
        break









        pressure = int(data_row[7].lstrip())