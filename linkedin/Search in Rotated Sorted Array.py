print(2)
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0

            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1

        def search(left, right):
            """
            Binary search
            """
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    return pivot
                else:
                    if target < nums[pivot]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
            return -1

        n = len(nums)

        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1

        rotate_index = find_rotate_index(0, n - 1)

        # if target is the smallest element
        if nums[rotate_index] == target:
            return rotate_index
        # if array is not rotated, search in the entire array
        if rotate_index == 0:
            return search(0, n - 1)
        if target < nums[0]:
            # search on the right side
            return search(rotate_index, n - 1)
        # search on the left side
        return search(0, rotate_index)









def method(nums,target):
    word_dic = {val:index for index,val in enumerate(nums)}
    def sort_arr(nums):
        res = []
        if len(nums) < 2:
            return nums
        split_val = nums[0]
        left = [num for num in nums if num < split_val]
        right = [num for num in nums if num > split_val]
        left = sort_arr(left)
        right = sort_arr(right)
        res += left
        res.append(split_val)
        res += right
        return res
    nums = sort_arr(nums)
    print(nums)
    s = 0
    e = len(nums) - 1
    while s < e:
        mid = s + (e - s) // 2
        if mid < target:
            s = mid + 1
        elif mid > target:
            e = mid - 1
        else:
            return word_dic.get(mid,-1)




def find_max_index(nums):
    if nums[0] < nums[-1]:
        return -1
    else:
        l = 0
        h = len(nums) - 1
        while l < h:
            mid = l + (h - l + 1) // 2
            if nums[mid] > nums[0]:
                l = mid
            else:
                h = mid -1
        return l

def find_value(nums, s, e, target):
    while s < e:
        mid = s + (e - s) // 2
        if nums[mid] == target:
            print(mid)
            return mid
        elif nums[mid] < target:
            s = mid + 1
        else:
            e = mid - 1

nums = [4,5,6,7,0,1,2]
target = 0
max_index = find_max_index(nums)
print(max_index)
if max_index == -1:
    find_value(nums, 0, len(nums) - 1, target)
else:
    if nums[0] > target:
        find_value(nums, max_index, len(nums) - 1, target)
    else:
        find_value(nums, 0, max_index, target)



# target = 3
# print(method(nums,target))


