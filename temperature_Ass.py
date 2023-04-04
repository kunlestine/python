def toCelsius(fahrenheit):
    """
    Accepts degrees Fahrenheit (fahrenhit argument)
    Returns degrees Celsius
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius
 
def toFahrenheit(celsius):
    """
    Accepts degrees Celsius (celsius argument)
    Returns degrees fahrenheit
    """
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit