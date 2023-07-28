def removeElement(nums, val):
    """
    takes an array of numbers and removes all numbers matching val
    """
    count = 0 
    j = len(nums)
    while count < j:
        if nums[count] == val:
            nums.pop(count)
            j -= 1
        else:
            count += 1
    return len(nums)