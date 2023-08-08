def isPerfectSquare(num):

    t = 1
    
    while t*t < num:
        t += 1
        if t*t == num:
            return True
        
    if num == 1: # Put the edge case here so it isn't checked every time
        return True
    
    return False 

def isPerfectSquareBin(num):
    if num == 1:
        return True

    left, right = 1, num // 2

    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid

        if square == num: 
            return True

        elif square < num:
            left = mid + 1

        else:
            right = mid - 1

    return False