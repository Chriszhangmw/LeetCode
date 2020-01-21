'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        used = [False] * len(nums)

        def helper(nums, temp):
            if len(nums) == len(temp):
                res.append(temp[:])
            for i in range(len(nums)):
                if used[i]: continue
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1]:
                    continue
                used[i] = True
                temp.append(nums[i])
                helper(nums, temp)
                used[i] = False
                temp.pop()

        helper(sorted(nums), [])
        return res

# 参考：https://www.cnblogs.com/zuoyuan/p/3758881.html






