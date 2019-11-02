'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
def method(n):
    dp = [1]*n
    for i in range(2,n):
        for j in range(i):
            dp[i] += dp[j]*dp[i-j-1]
    return dp,dp[n-1]

a,b = method(7)
print(a)
print(b)












