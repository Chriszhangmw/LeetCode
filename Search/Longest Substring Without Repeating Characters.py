'''

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

import collections
from collections import deque
def method(s):
    seen = set()
    max_len = 0
    dp = deque()
    for e in s:
        if e in seen:
            k = None
            while k != e:
                k = dp.popleft()
                seen.remove(k)
        dp.append(e)
        seen.add(e)
        max_len = max(max_len,len(dp))
    return max_len


s = 'abcabcbb'
print(method(s))










