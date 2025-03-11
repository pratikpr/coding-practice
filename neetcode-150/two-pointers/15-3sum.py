# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l,r = i+1, len(nums)-1
        target = -nums[i]
        while l < r:
            _sum = nums[l] + nums[r]
            if _sum == target:
                res.append([nums[i], nums[l], nums[r]])
                l += 1; r -= 1
                # while l < r and nums[l] == nums[l-1]:
                #         l += 1
            elif _sum > target:
                r -= 1
            else:
                l += 1
    return res


nums = [-1,0,1,2,-1,-4,1] #sort: [-4,-1,-1,0,1,1,2]
print(threeSum(nums))
