def plusOne(digits):
    
    i = -1 

    while digits[i] == 9 and i > -len(digits): 
        i -= 1
        
    if digits[i] == 9:
        digits = [1] + [0]*len(digits)
        
    elif i == -1:
        digits[-1] += 1
        
    else:
        digits[i] += 1
        digits = digits[:i + 1] + [0]*(-i - 1)
    
    return digits 

nums = [1, 5, 6, 1]

nums2 = [9, 5, 2, 9]

nums3 = [9, 9, 9, 9]