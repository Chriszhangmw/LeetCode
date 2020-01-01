'''
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words,
one of the first string's permutations is the substring of the second string.



Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
'''


def checkInclusion(s1: str, s2: str) -> bool:
    import collections
    s1map = collections.defaultdict(int)
    s2map = collections.defaultdict(int)
    for e in s1:
        s1map[e] += 1
    for ee in s2[:len(s1)]:
        s2map[ee] += 1
    i = 0
    j = len(s1)
    while j < len(s2):
        if s1map == s2map:
            return True
        s2map[s2[i]] -= 1
        if s2map[s2[i]] == 0:
            s2map.pop(s2[i])
        s2map[s2[j]] += 1
        i += 1
        j += 1
    return s1map == s2map








s2 = 'eidbaooo'
s1 = 'ab'
print(checkInclusion(s1,s2))






