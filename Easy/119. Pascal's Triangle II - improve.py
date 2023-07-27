import math
def getRow(rowIndex):
    """
    Takes a row index and returns the desired row of Pascal's triangle using the fact
    that each row is an array of binomial coefficients
    
    Arguments:
    rowIndex (int): Index of a desired row of Pascal's triangle
    
    Returns:
    row (1darray) : the indexed row of Pascal's Triangle
    """


    row = []

    for i in range(rowIndex+1):
        num = (math.factorial(rowIndex))/(math.factorial(rowIndex-i)*math.factorial(i))
        row.append(num)
        
    return row


# Slow solution because of all the factorials, would be easier just to construct the triangle up to that point and only return the desired row