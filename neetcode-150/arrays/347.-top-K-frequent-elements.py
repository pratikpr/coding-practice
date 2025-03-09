# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

from typing import List
from collections import Counter
import heapq


def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq_map = Counter(nums)
    k_freq = heapq.nlargest(k, freq_map.items(), key=lambda x: x[1])
    
    return [item[0] for item in k_freq]

nums = [1,1,1,2,2,3]; k = 2
print(topKFrequent(nums, k))
        