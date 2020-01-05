'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''

def numDecodings(nums):

    dp = [0] * len(nums)

    dp[0] = 1

    for i in range(1,len(nums)):
        if int(nums[i-1] + nums[i]) <= 26:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]
    print(dp[-1])

nums = '12'
numDecodings(nums)

















