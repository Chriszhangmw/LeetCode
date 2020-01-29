'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        res = [-1, -1]

        low = 0
        high = length - 1

        if length == 0:
            return res
        if target < nums[low] or target > nums[high]:
            return res

        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                low = mid
                high = mid
                while (low - 1) >= 0 and nums[low - 1] == target:
                    low -= 1
                while (high + 1) < length and nums[high + 1] == target:
                    high += 1
                break
        if nums[low] == target:
            res[0] = low
            res[1] = high
        return res

