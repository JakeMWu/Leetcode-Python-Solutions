def majorityElement(self, nums):
    for num in set(nums):
        if nums.count(num) > len(nums)/2:
            return num 