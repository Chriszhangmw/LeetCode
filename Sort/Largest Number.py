
'''
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
'''

def method(nums):
    if len(nums) < 2:
        return nums
    midvalue = nums[0]
    left = [i for i in nums if int(str(i)+str(midvalue)) < int(str(midvalue)+str(i)) ]
    right = [i for i in nums if int(str(i)+str(midvalue)) > int(str(midvalue)+str(i))]
    res = []
    left = method(left)
    right = method(right)
    res+=right
    res.append(midvalue)
    res+=left
    return res
nums = [3,30,34,5,9]
a = method(nums)
# a=''.join(a)
print(a)













