'''
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
注意这个case：
[1,2,4,8,9,72]
到72的时候，往前找到9，可以整除，更新dp[5]为max(1, 2 + 1) = 3,
注意此时应该继续往前找，不能停，直到找到8,发现dp[3] + 1 = 5 > 3，于是更新dp[i]
注意就是不能停，找到一个能整除并不够，前面有可能有更大的啊~~

'''

def largestDivisibleSubset(nums):
    N = len(nums)
    nums.sort()
    dp = [0]*N
    parent = [0] * N
    mx = 0
    mx_index = -1
    for i in range(N):
        for j in range(i-1,-1,-1):
            if nums[i]%nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                parent[i] = j
                if dp[i] > mx:
                    mx = dp[i]
                    mx_index = i
    res = list()
    for k in range(mx+1):
        res.append(nums[mx_index])
        mx_index = parent[mx_index]
    print(res)
    print(res[::-1])



nums = [1,2,4,8,9,12,5]
largestDivisibleSubset(nums)















