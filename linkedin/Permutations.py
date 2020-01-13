'''

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 相当于是全排列的问题，还有一个排列，也请记住

        if len(nums) <= 1:
            return [nums]

        res = []
        for i in range(len(nums)):
            sub_nums = nums[:i] + nums[i + 1:]
            for e in self.permute(sub_nums):
                res.append([nums[i]] + e)

        # def helper(nums):
        #     if len(nums) < 2:
        #         return nums
        #     for i in range(len(nums)):
        #         sub_nums = nums[:i] + nums[i+1:]
        #         new_nums = helper(sub_nums)
        #         for e in new_nums:
        #             res.append([nums[i]] + e)
        # res = []
        # helper(nums)
        return res