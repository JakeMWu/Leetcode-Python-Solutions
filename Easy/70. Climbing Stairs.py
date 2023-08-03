def climbStairs(n):
    """
    Given a number of stairs, gives the number of ways that one can 
    ascend the stairs in combinations of 1 and 2 steps
    """
    if n == 1:
        return 1
    
    elif n == 2: 
        return 2
    
    n_2 = 1
    n_1 = n_2
    
    for i in range(n-2):
        n_3 = n_1 + n_2 
        
        n_2 = n_1 
        n_1 = n_3
        
    return n_3
    
# Surprised this was an easy problem, it's easy to code after 
# recognizing the sequence but solving that problem isn't necessarily