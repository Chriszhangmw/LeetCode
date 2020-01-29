'''
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
'''


class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            return self.myPow(1 / x, -n)
        if n == 0:
            return 1
        if n == 2:
            return x * x
        return self.myPow(self.myPow(x, n / 2), 2) if not n % 2 else x * self.myPow(self.myPow(x, n // 2), 2)

#         def helper(x,n):
#             res = 1.0
#             if n==1:
#                 return x*res
#             res = res*x * helper(x,n-1)
#         return res

#         if n < 0:
#             x = 1/x
#             n = -n
#         res_ = helper(x,n)
#         return res_









