def merge(self, nums1, m, nums2, n):
    """
    Takes two integer arrays, nums1 and nums2 and merges them in nums1. Nums1 has trailing zeros
    in order to accomoddate this
    """
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0: 
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1 
        else:
            nums1[k] = nums2[j]
            j -= 1 
            
        k -= 1

    # We only need to account for j as if i>=0, the items are already in place
    while j >= 0:
        nums1[k] = nums2 [j]
        j -= 1
        k -= 1

    return nums1