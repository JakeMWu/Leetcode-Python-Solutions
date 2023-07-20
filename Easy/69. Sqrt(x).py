def mySqrt(x):
    """
    Finds the closest integer below the square root of x by squaring the integers iteratively
    
    Arguments:
        x (int)
        
    Returns: 
        min-1 (int): an integer which is either the sqrt of x or the closest integer less than x
        
    """

    i = 0
    
    while i*i <= x: 
        i += 1
    
    return i-1

# Attempt 2

def mySqrt1(x):
    """
    Finds the closest integer below the square root of x through binary search
    
    Arguments:
        x (int)
        
    Returns: 
        min-1 (int): an integer which is either the sqrt of x or the closest integer less than x
        
    """
    if x == 0 or x == 1:
            return x
        
    min = 0
    max = x//2
    
    while min <= max:
        middle = (min+max)//2 
        if middle*middle == x: 
            return middle 
        
        elif middle*middle <= x:
            min = middle + 1
        
        elif middle*middle > x:
            max = middle - 1
    
    return min - 1