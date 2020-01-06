'''
将一个二维数组排列成金字塔的形状，找到一条从塔顶到塔底的路径，使路径上的所有点的和最小，从上一层到下一层只能挑相邻的两个点中的一个。
注意点：

最好将空间复杂度控制在O(n)，n是金字塔的高度
例子:

输入:

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
输出: 11 (2 + 3 + 5 + 1 = 11)
'''

def method(nums):

    dp = [0] * len(nums)

    dp[0] = nums[0][0]
    for i in range(1,len(nums)):
        array_curr = nums[i]
        dp[i] = dp[i-1] + min(array_curr)
    print(dp[-1])

nums = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
method(nums)

def minimumTotal(triangle):
    n = len(triangle)
    dp = triangle[-1]
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            dp[j] = triangle[i][j] + min(dp[j] , dp[j+1])
    return dp[0]










