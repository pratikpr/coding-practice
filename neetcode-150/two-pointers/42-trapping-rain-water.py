# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

from typing import List


def trap(height: List[int]) -> int:
    l, r = 0, len(height)-1
    left_max, right_max = 0, 0
    res = 0
    
    while l < r:
        if height[l] <= height[r]:
            if height[l] >= left_max:
                left_max = height[l]
            else:
                res += left_max-height[l]
            l += 1
        else:
            if height[r] >= right_max:
                right_max = height[r]
            else:
                res += right_max-height[r]
            r -= 1
                
    return res

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))

height = [4,2,0,3,2,5]
print(trap(height))
