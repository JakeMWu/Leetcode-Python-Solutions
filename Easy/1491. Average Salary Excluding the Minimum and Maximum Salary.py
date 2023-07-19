def average(salary):
    """
    Takes an array of salaries and takes the mean excluding the maximum and minimum salaries

    Arguments:
    salary (1darray)
    
    Returns:
    sum/(len(salary)-2) (float): mean of items in the array exlcuding max and min
    """
    
    max = 0.0
    min = salary[0]
    sum = 0.0
    
    for i in range(len(salary)):
        
        sum += salary[i]
        
        if salary[i] > max:
            max = salary[i]
        
        elif salary[i] < min:
            min = salary[i]
        
    sum = sum - max - min
    
    return sum/(len(salary)-2)
