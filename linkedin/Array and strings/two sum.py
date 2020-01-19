'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic = {}
        for i in range(len(nums)):
            num_dic[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_dic.keys() and num_dic[complement] != i:
                return [i, num_dic[complement]]
        return [-1, -1]








