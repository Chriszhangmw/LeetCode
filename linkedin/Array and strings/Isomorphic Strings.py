'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
'''


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #         if len(s) != len(t):
        #             return False

        #         import collections
        #         scounter = collections.defaultdic(int)
        #         tcounter = collections.defaultdic(int)
        #         for i in range(len(s)):
        #             scounter[s[i]] += 1
        #             tcounter[t[i]] += 1
        #         for index,value in scounter.items():
        #             if value != tcounter[index]:
        #                 return False
        #         return True

        map_st = {}
        for i in range(len(s)):
            si = s[i]
            ti = t[i]
            if si in map_st.keys():
                if map_st[si] != ti:
                    return False
            else:
                if ti in map_st.values():
                    return False
                map_st[si] = ti
        return True









