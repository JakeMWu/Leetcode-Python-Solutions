def removeDuplicates(nums):
    """
    Takes a strictly non-decreasing array "nums" and removes duplicates in-place and returns 
    the number of unique values

    Parameters
    ----------
    nums (1darray): strictly non-decreasing array

    Returns
    len(nums) (int): number of unique values in nums

    """
    no_dupes = [nums[0]]
    for i in range(len(nums)):
        if nums [i] > no_dupes[-1]:
            no_dupes.append(nums[i])
    nums[:] = no_dupes
    return len(nums)