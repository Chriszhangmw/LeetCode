'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

'''


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates = sorted(candidates)

        def dfs(candidates, sublist, target, last):
            if target == 0:
                res.append(sublist[:])
            if target < candidates[0]:
                return
            for n in candidates:
                if n < last:
                    continue
                if n > target:
                    return
                sublist.append(n)
                dfs(candidates, sublist, target - n, n)
                sublist.pop()

        dfs(candidates, [], target, candidates[0])
        return res





