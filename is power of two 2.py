import math 

def isPowerOfTwo(n):
    if math.log2(n) % 1 == 0:
        return True
    else: 
        return False 

