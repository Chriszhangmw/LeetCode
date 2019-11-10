'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
'''

def quick(nums):
    if len(nums) < 2:
        return nums
    v = nums[0]
    left = [i for i in nums if i < v]
    right = [i for i in nums if i > v]
    left = quick(left)
    right = quick(right)
    res = []
    res+=left
    res.append(v)
    res+=right
    return res

def method(num1,num2):
    num1 = quick(num1)
    num2 = quick(num2)
    k = []
    for i in num1:
        if i in num2:
            k.append(i)
    print(k)

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
method(nums1,nums2)









