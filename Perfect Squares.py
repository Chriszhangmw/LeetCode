'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''
import collections
class Solution:
    def numSquares(self,n):
        dp = collections.defaultdict(int)
        y = 1
        while y*y <= n:
            dp[y*y] = 1
            y +=1
        for x in range(1,n+1):
            y = 1
            while x + y*y <= n:
                if x + y*y not in dp or dp[x]+1 < dp[x+y*y]:
                    dp[x + y*y] = dp[x]+1
                y +=1
        return dp[n]


a = Solution()
print(a.numSquares(8))














