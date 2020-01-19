'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        import collections
        res = ''
        if not s or not t:
            return res
        left, cnt, minLen = 0, 0, len(s) + 1
        tcount = collections.Counter(t)
        scount = collections.defaultdict(int)  # 这里的counter维护窗口内的字符串
        right = 0
        while right < len(s):
            scount[s[right]] += 1
            if s[right] in tcount and scount[s[right]] <= tcount[s[right]]:
                cnt += 1
            while left <= right and cnt == len(t):
                if minLen > right - left + 1:
                    minLen = right - left + 1
                    res = s[left:right + 1]
                scount[s[left]] -= 1
                if s[left] in tcount and scount[s[left]] < tcount[s[left]]:
                    cnt -= 1
                left += 1
            right += 1
        return res


