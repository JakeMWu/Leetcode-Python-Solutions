def isPowerOfTwo(n):
    if n ==1: 
        return True
    else:
        new_num = n 
        while new_num / 2 >= 1:
            if new_num / 2 != 1:
                new_num = new_num/2
            
            else: 
                return True
            
        return False
    
print(isPowerOfTwo(1))