"""Unit tests for climate.py"""

__author__ = 'Adekunle Adeoya'

import unittest

import climate 
import temperature


class TestClimate(unittest.TestCase):
    """Test case for the climate functions"""

    def test_climate_heating_degree_days_1(self):
        """Test the heating degree days function
        
        Test the case when mean temperature is 18
        """
        self.assertEqual(0, climate.heating_degree_days(18))

    def test_climate_heating_degree_days_2(self):
        """Test the heating degree days function
        
        Test the case when mean temperature is greater than 18
        """
        self.assertEqual(0, climate.heating_degree_days(20.5))

    def test_climate_heating_degree_days_3(self):
        """Test the heating degree days function
        
        Test the case when mean temperature is less than 18
        """
        self.assertEqual(2.5, climate.heating_degree_days(15.5))

    def test_climate_heating_degree_days_4(self):
        """Test the heating degree days function
        
        Test the case when mean temperature is less than 18 and negative
        """
        self.assertEqual(28.0, climate.heating_degree_days(-10.0))
