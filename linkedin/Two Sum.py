
print('kkkkkkkkk')
'''

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''


def two_sum(nums,target):
    store = {}
    for index,num in enumerate(nums):

        if target - num in store:
            return [index,store[target-num]]
        if num not in store:
            store[num] = index

def twoSum( nums, target):
    h = {}
    for i, num in enumerate(nums):
        n = target - num
        if n not in h:
            h[num] = i
        else:
            return [h[n], i]
nums = [2,7,11,15]
target = 9

print(twoSum(nums,target))






