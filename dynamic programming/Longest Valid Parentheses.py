'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''


def longestValidParentheses(s):
    if not s:
        return 0
    length = len(s)
    dp = [0 for _  in range(length)]

    for i in range(1,length):
        if s[i] == ')':
            if s[i-1] == '(':
                dp[i] = dp[i-2] + 2
            if s[i-1] == ')':
                if i-dp[i-1]-1 >0 and s[i-1-dp[i-1]] == '(':
                    dp[i] = dp[i-1] + dp[i-dp[i-1] - 2] + 2
                else:
                    dp[i] = dp[i-1] + 2
    return max(dp)









