'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''


class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A) == 0:
            return 0
        min_tmp = A[0]
        max_tmp = A[0]
        result = A[0]
        for i in range(1, len(A)):
            a = A[i] * min_tmp
            b = A[i] * max_tmp
            c = A[i]
            max_tmp = max(max(a,b),c)
            min_tmp = min(min(a,b),c)
            result = max_tmp if max_tmp > result else result
        return result

#分三中情况一一讨论就很容易得到答案
#只有正数
#只有正数和0
#正数，负数，0都有，需要明白如果遍历到某个数是负数的时候，此时需要有两个
#指针来记录最大值和最小值，遇到负数，这两个值就刚好交换位置了