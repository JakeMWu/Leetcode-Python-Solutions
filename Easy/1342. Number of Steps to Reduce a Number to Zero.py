def numberOfSteps(num):
    """
    Takes a positive integer and returns the number of steps it takes 
    for that integer to reach zero according to the following algorithm
    1. If the number is even divide it by 2
    2. If the number is odd subtract 1
    3. If the number is greater than zero go to step 1
    """
    j=0
    while num!=0:
        j+=1
        if num % 2 == 0:
            num = num/2
            
        else:
            num -= 1
            
    return j