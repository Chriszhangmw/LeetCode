'''

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
'''
import sys

def method(nums,k):
    left = 0
    Sum = 0
    res = sys.maxsize
    for i in range(len(nums)):
        Sum += nums[i]
        while Sum >= k:
            res = min(res, i - left + 1)
            Sum -= nums[left]
            left += 1
    if res == sys.maxsize:
        return 0
    return res


nums = [2,3,1,2,4,3]
k = 7


def method2(nums,k):
    pass



print(method(nums,k))












