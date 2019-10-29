'''
给定一个字符串（s）和一个正则表达式（p），判断字符串和正则表达式是否匹配。在本问题中，正则表达式仅仅支持‘.’和‘*’这两种符号。
Note：
i.‘.’匹配任意单一字母。
ii.‘*’匹配0次或者多次‘*’之前的那个字母。
iii. 字符串s可以为空，只包含a-z的字母。
iv. 正则表达式p可以为空，只包含a-z以及符号‘.’和‘*’。
Examples1：
输入：
s = "aa"
p = "a"
输出：false
Example 2：
输入：
s = "aa"
p = "a*"
输出：true
解释：“a*”表示匹配0次或者多次‘a’，如果匹配两次‘a’，我们就得到了“aa”。
Example 3：
输入：
s = "ab"
p = ".*"
输出：true
解释：".*"表示匹配0次或者多次‘.’，也就是匹配0次或者多次任意字母的意思，所以可以匹配一次‘a’再匹配一次‘b’，我们就得到了“ab”。
Example 4：
输入：
s = "aab"
p ="c*a*b"
输出: true
解释：“c*”匹配0次‘c’，“a*”匹配两次‘a’，‘b’匹配‘b’，我们就得到了“aab”。
'''

import numpy as np

def method1(s,p):
    m = len(s)
    n = len(p)
    # dp = np.zeros((m,n))
    dp = [[False for i in range(m)] for j in range(n)]
    dp[0][0] = True
    for i in range(m):
        dp[i][0] = False
    for j in range(n):
        if j%2 == 0:
            if (dp[0][j-2]) and p[j-1]=='*':
                dp[0][j] = True
        else:
            dp[0][j] = False

    for i in range(m):
        for j in range(n):
            if p[j-1] == '.':
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i][j-1] or (dp[i][j-2] and p[j-2]=='.')
            else:
                dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]
            # if p[j-1] != '*':
            #     if (s[i-1] == p[j-1] or p[j-1] == '.') and  dp[i-1][j-1]:
            #         dp[i][j] = True
            # else:
            #     if dp[i][j-2] or ((s[i-1]==p[j-2] or p[p-2]=='.') and dp[i-1][j]):
            #         dp[i][j] = True
    return dp



print(method1('',''))





















