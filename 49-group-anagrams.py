# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    word_map = {}
    
    # for more efficiency use a count array; reduces NKlogK to NK
    for word in strs:
       sorted_word = ''.join(sorted(word))
       word_map.setdefault(sorted_word, []).append(word)
       
    return [_list for _list in word_map.values()]

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))

strs = ["a"]
print(groupAnagrams(strs))

