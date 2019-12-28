'''
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:

Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
1
2
3
4
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
'''

from functools import reduce

def method1(nums,k):
    res = 0
    for i in range(len(nums) + 1):
        for j in range(len(nums) + 1):
            if nums[i:j]:
                cureent_sum = reduce(lambda x,y:x * y,nums[i:j])
                if cureent_sum < k:
                    # print(nums[i:j])
                    res += 1
    print(res)


nums = [10, 5, 2, 6]
k = 100
# print(method1(nums,k))

def methos_slid(nums,k):
    N = len(nums)
    prod = 1
    l,r = 0,0
    res = 0
    while r < N:
        prod *= nums[r]
        while l <= r and prod >= k:
            prod /= nums[l]
            l +=1
        res += r - l + 1
        r += 1
    print(res)




methos_slid(nums,k)


