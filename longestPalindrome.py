'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

'''

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Return if string is empty
        if not s: return s

        res = ""
        for i in range(len(s)):
            j = i + 1
            # While j is less than length of string
            # AND res is *not* longer than substring s[i:]
            while j <= len(s) and len(res) <= len(s[i:]):
                # If substring s[i:j] is a palindrome
                # AND substring is longer than res
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(res):
                    res = s[i:j]
                j += 1

        return res


class Solution2:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_ = [1]*len(s)
        for i in range(len(s)):
            count1 = count2 = 1
            if i+1<len(s) and s[i] == s[i+1]:
                mid = 1
                count1 = 2
                while i-mid>=0 and i+1+mid<len(s) and s[i-mid] == s[i+1+mid]:
                    count1 += 2
                    mid += 1
            if i-1>=0 and i+1<len(s) and s[i-1] == s[i+1]:
                mid = 1
                count2 = 1
                while i-mid>=0 and i+mid<len(s) and s[i-mid] == s[i+mid]:
                    count2 += 2
                    mid += 1
            list_[i] = max(count1,count2)
        max_ = index = 0
        for j in range(len(list_)):
            if max_ < list_[j]:
                max_ = list_[j]
                index = j
        if max_ % 2 == 0:
            return s[index-max_//2+1:index+1+max_//2]
        else:
            return s[index-(max_+1)//2+1:index+(max_+1)//2]
