# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

from typing import List


def longestConsecutive(nums: List[int]) -> int:
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        if num-1 not in num_set:
            current = 1
            curr_num = num
            
            while curr_num+1 in num_set:
                curr_num += 1
                current += 1
            
            longest = max(longest, current)
            
    return longest

nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))
    