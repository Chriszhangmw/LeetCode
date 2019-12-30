'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

def pan(w,s2):
    flag = True
    if len(w) == len(s2):
        for i in w:
            if i not in s2:
                flag = False
    return flag


def method(s1,s2):
    import collections
    ans = []
    scounter = collections.Counter()
    pcounter = collections.Counter(s2)
    len1 = len(s1)
    len2 = len(s2)
    for i in range(len1):
        scounter[s1[i]] +=1
        if i >= len2:
            scounter[s1[i-len2]] -=1
            if scounter[s1[i-len2]] == 0:
                del scounter[s1[i-len2]]
        if scounter == pcounter:
            ans.append(i-len2 + 1)
    return ans



s1 = "cbaebabacd"
s2 = "abc"

print(method(s1,s2))

















