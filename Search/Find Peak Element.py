'''

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.

'''


def method(nums):
    left = 1
    res = []
    while left < len(nums)-1:
        if nums[left] < nums[left-1]:
            left +=1
            continue
        else:
            if nums[left] > nums[left+1]:
                res.append(left)
                left +=2
            else:
                left +=1
    print(res)




def method2(nums):
    left = 1
    right = len(nums) -1
    mid = left + (right - left) // 2
    if nums[mid] > nums[mid-1] and nums[mid] > nums[mid + 1]:
        return mid
    elif nums[mid - 1] > nums[mid]:
        return method2(nums[:mid])
    else:
        return method2(nums[mid+1:])


    # while left < right:
    #     mid = left + (right - left)//2
    #     if nums[mid]





nums = [1,2,1,3,5,6,4]
print(method2(nums))














