print('jjjj')
'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the
 largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
        0, 1,-2,4, 
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, 
which is more subtle.
'''



def maxSubArray(nums):
    dp = [0 for _ in range(len(nums))]
    dp[0] = max(nums[0],0)
    for i in range(1,len(nums)):
        if dp[i-1] == 0:
            if nums[i] > 0:
                dp[i] = nums[i]
        if dp[i-1] > 0:
            if nums[i] < 0:
                dp[i] = max(dp[i-1] + nums[i], 0)
            else:
                dp[i] = dp[i-1] + nums[i]
    print(dp[-1])
    print(dp)
    return dp[-1]



nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArray(nums)












