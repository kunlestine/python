__author__ = "Adeoya Adekunle"

from os import environ
import os

environ['PROJ_LIB'] = 'C:\\Users\\W0475475\\.conda\\envs\\prog5000\\Library\\share\\proj'

import csv
import pyproj
from pyproj import crs


class BoundingBox:
    """ a boundingbox"""
    

    def __init__(self, name:str,  minx: int, miny:int, maxx:int, maxy:int, crs:pyproj.CRS ):
    # The min and max points
        self.name = name
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy
        self.crs = crs
    

    @classmethod
    def from_filepath(cls, filepath, name:str):
        # split the path
        # head and tail pair 
        head_tail = os.path.splitext(filepath)
        # joining  the file path by string concatenation
        head = head_tail[0] + '.prj'
        # Opening the bounds.prj
        with open(head, 'r') as bound:
            reader = bound.read()
            #print(reader)
            # importing the crs from pyproj
            crs_1 = crs.CRS.from_wkt(reader) 
        #Opening  the filepath
        with open(filepath, 'r') as file:
            csv_reader = csv.reader(file, delimiter=',')
            header = next(csv_reader)
            for row in csv_reader:
                if name == row[0]:
                    return cls(name, row[1], row[2], row[3], row[4],crs_1)


    def transform_to (self, crs_1):
        transformer = pyproj.Transformer.from_crs(self.crs, crs_1, always_xy = True)
        x2, y2 = transformer.transform(self.minx, self.miny)
        print( x2, y2)

        
if __name__ == "__main__":
    # instantiate the class - this uses the init method
    # of the class
    bounding_box_1 = BoundingBox.from_filepath('D:\\python\\Assignment_3\\data\\bounds.csv', 'BBOX-1')
    #print(bounding_box_1.name, bounding_box_1.minx, bounding_box_1.crs)
    bounding_box_1.transform_to (bounding_box_1.crs)
   
    with open('D:\\python\\Assignment_3\\data\\geolocation.csv', 'r') as geolocation:
        head_tail2 = os.path.splitext(geolocation)
        head_2 = head_tail2[0] + '.prj'
        with open (head_2, 'r') as location:
            reader_2 = location.read()



        




