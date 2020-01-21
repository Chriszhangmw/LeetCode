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
        res = []
        used = [False] * len(nums)

        def helper(nums, temp):
            if len(temp) == len(nums):
                res.append(temp[:])
            for i in range(len(nums)):
                if used[i]: continue
                used[i] = True
                temp.append(nums[i])
                helper(nums, temp)
                used[i] = False
                temp.pop()

        helper(sorted(nums), [])
        return res

        # 相当于是全排列的问题，还有一个排列，也请记住

#         if len(nums) <= 1:
#             return [nums]

#         res = []
#         for i in range(len(nums)):
#             sub_nums = nums[:i] + nums[i+1:]
#             for e in self.permute(sub_nums):
#                 res.append([nums[i]] + e)

#         # def helper(nums):
#         #     if len(nums) < 2:
#         #         return nums
#         #     for i in range(len(nums)):
#         #         sub_nums = nums[:i] + nums[i+1:]
#         #         new_nums = helper(sub_nums)
#         #         for e in new_nums:
#         #             res.append([nums[i]] + e)
#         # res = []
#         # helper(nums)
#         return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            s = nums[:i] + nums[i + 1:]
            p = self.permute(s)
            for x in p:
                res.append([nums[i]] + x)
        return res

        # res = []
        # used = [False] * len(nums)
        # def helper(nums,temp):
        #     if len(temp) == len(nums):
        #         res.append(temp[:])
        #     for i in range(len(nums)):
        #         if used[i]:continue
        #         used[i] = True
        #         temp.append(nums[i])
        #         helper(nums,temp)
        #         used[i] = False
        #         temp.pop()
        # helper(sorted(nums),[])
        # return res

        # 相当于是全排列的问题，还有一个排列，也请记住

#         if len(nums) <= 1:
#             return [nums]

#         res = []
#         for i in range(len(nums)):
#             sub_nums = nums[:i] + nums[i+1:]
#             for e in self.permute(sub_nums):
#                 res.append([nums[i]] + e)

#         # def helper(nums):
#         #     if len(nums) < 2:
#         #         return nums
#         #     for i in range(len(nums)):
#         #         sub_nums = nums[:i] + nums[i+1:]
#         #         new_nums = helper(sub_nums)
#         #         for e in new_nums:
#         #             res.append([nums[i]] + e)
#         # res = []
#         # helper(nums)
#         return res