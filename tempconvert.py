def temp_convert (F):
    '''(number)->number
    Returns a temperature in celsius from a farhenheit temperature
    >>> temp_convert(78)
    24.0
    '''
    converter = (F-32)*(5/9)

    return converter
