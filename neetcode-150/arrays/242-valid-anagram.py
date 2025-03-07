# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

def isAnagram(s: str, t: str) -> bool:
    s_freq = {}
    
    for c in s:
        s_freq[c] = s_freq.get(c, 0) + 1
        
    for c in t:
        if c not in s_freq or s_freq[c] <= 0:
            return False
        s_freq[c] -= 1
    
    return True if sum(s_freq.values()) == 0 else False

s = 'star'; t = 'tar'
print(isAnagram(s, t))