def isHappy(self, n):
    """
    Given an integer n determines whether n is a happy number where a happy number 
    is a number which terminates in a loop where the result is one when the happy algorithm is applied. The algorithm
    takes each individual digit of n, squares them and sums those squares to generate a new number

    arguments:
    n (int)
    
    outputs:
    True/False 
    """
    past_num = []
    while True:
        if n in past_num:
            return False
        
        elif n == 1:
            return True
        
        else:
            past_num.append(n)
            m = str(n)
            n = 0 
            for char in m:
                n += int(char)**2