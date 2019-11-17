'''
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
'''

def method(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return i

print(method([0,1,0]))




def method2(nums):
    left,right = 0,len(nums)-1
    while left < right:
        mid = (left + right)/2
        if nums[mid -1] < nums[mid] and nums[mid] < nums[mid + 1]:
            left = mid
        elif nums[mid -1] > nums[mid] and nums[mid] > nums[mid + 1]:
            right = mid
        else:
            break
    return mid

def method3(nums):
    left = 0
    right = len(nums)
    while left < right:
        mid = left + (right - left)//2
        if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
            return mid
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return -1
