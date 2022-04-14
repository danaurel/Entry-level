def perimeter (side1, side2, side3):
    '''(number, number, number) -> number
    Return the perimeter of the triangle with sides of length side1, side2 and side3.
    
    >>> perimeter(3, 4, 5)
    12
    >>> perimeter(10.5,6,9.3)
    '''
    
    
    return side1 + side2 + side3
	
	
# Make a new function that will calculate the semiperimeter.

def semiperimeter (side1, side2, side3):
    '''(number) -> number
	
    Return the semiperimeter of a triangle with sides 1, side2, side3
	
    >>> semiperimeter(3,4,5)
    6.0
    >>> semiperimeter (10.5,6,9.3)
    12.9
    '''
	
    return perimeter (side1, side2, side3)/2
