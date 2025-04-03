def count_pairs(nums, target):
    nums.sort()
    l, r = 0, len(nums)-1
    count = 0
    
    while l < r:
        _sum = nums[l] + nums[r]
        if _sum < target:
            count += (r-l)
            l += 1
        else:
            r -= 1
    return count
    
nums = [1, 3, 5, 7]; target = 8
print(count_pairs(nums, target))
