def add_two(nums, target):
    for i in range (0, len(nums) - 1):
        for j in range(1, len(nums) - (i)):
            if nums[i] + nums [i + j] == target:
                target_pair = [nums[i], nums[i + j]]
                return target_pair