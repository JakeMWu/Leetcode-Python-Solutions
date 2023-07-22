def kthFactor(n, k):
    """
    Takes an integer n, and returns either the kth factor, if it exists, or returns -1. There is a more efficient solution - 
    
    Arguments:
    n (int): target number 
    k (int): target factor
    
    Returns:
    -1 (int): if the kth factor doesn't exist
    factors[k-1]: the kth factor if it exists
    """
    factors = []
    for i in range(1, (n//2)+1): # +1 accounts for edge case of n=2
        if n % i == 0:
            factors.append(i)
    factors.append(n)
    if len(factors) < k:
        return -1
    else: 
        return factors[k-1]