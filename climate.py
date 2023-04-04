"""Climate functions
Functions based on the ECCC glossary definitions
found at:

https://climate.weather.gc.ca/glossary_e.html
"""

__author__ = 'Adeoya Adekunle Babafemi'

import argparse
import temperature


"""
    Calculating the maximum and minimum temperature 
    of heating degree day Degree-days for a given day represent 
    the number of celsius degrees that the mean temperature
    is above or below base temperature.
    heating degree-days are the number of degree below 18c. 
    if the temperature is equal to or greater than 18c, 
    then the number will be zero.
"""

def heating_degree_days(mean_temperature: float) -> float:
    constant_temperature = 18
    if mean_temperature < constant_temperature:

        heating_degree_day = constant_temperature - mean_temperature
        return heating_degree_day
    elif mean_temperature >= constant_temperature:
        return 0


if __name__ == '__main__':    
    my_parser = argparse.ArgumentParser(description='heating_degree_days')
    # An argument for the minimun temperature of heating degree days
    my_parser.add_argument('min_temp', type=float, 
        help='The minimum temperature of heating day')
    my_parser.add_argument('max_temp', type=float, 
        help='The maximum temperature of heating day')
    my_parser.add_argument('from_unit', type=str,
        choices=['celsius', 'c', 'C', 'Celsius', 'f','fahrenreit'],
        help='the unit of the mean temperature argument')
    # Parse the arguments
    args = my_parser.parse_args()
    
    # Calculating the mean temperature 
    mean_temperature = (args.min_temp + args.max_temp)/ 2
    # Calling the heating degree days and assigning it to a new variable  
    heating_days = heating_degree_days(mean_temperature)
    # Assigning unit argument to a new variable
    unit = args.from_unit
   
    if unit == 'fahrenheit' or unit == 'f':
        result = temperature.fahrenheit_to_celsius(mean_temperature)
        heating_degree_days_celsius = heating_degree_days(result)

        print(f'The mean temperature is {mean_temperature} {unit}\
              which results in { heating_degree_days_celsius * 1.8} heating degree-days')
    else:
        print(f'The mean temperature is {mean_temperature} {unit}\
              which results in {heating_days } heating degree-days')
    
    
    