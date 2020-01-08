'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

'''

def word_break(s,wordDict):
    n = len(s)
    dp = [False for _ in range(n+1)]
    dp[0] = True
    for i in range(1,n+1):
        for j in range(i,-1,-1):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    print(dp[n])



# s = "applepenapple"
# wordDict = ["apple", "pen"]
#
# word_break(s,wordDict)

'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
'''




# dynamic programming and DFS

def wordBreak_second(s,wordDict):
    res = []

    def dfs(s,stringlist):
        if check(s):
            if len(s) == 0:
                res.append(stringlist[1:])
            for i in range(1,len(s)+1):
                if s[:i] in wordDict:
                    dfs(s[i:],wordDict,stringlist + ' ' + s[:i])

    def check(s):
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(len(s)):
            for j in range(i,-1,-1):
                if dp[j] and s[j:i+1] in wordDict:
                    dp[i+1] = True
                    break
        return dp[len(s)]










# def word_break_2(s,wordDict,res,path):
#     length = len(s)
#     if length == 0:
#         return []
#     s = 0
#     n = length-1
#     for i in range(n):
#         if i > 0:
#             for j in range(i):
#                 if s[j:i+1] in wordDict:
#                     path += [s[j:i+1]]
#     res.append(path)
#
#
#
#
#     n = len(s)
#     dp = [False for _ in range(n+1)]
#     dp[0] = True
#     for i in range(1,n+1):
#         for j in range(i,-1,-1):
#             if dp[j] and s[j:i] in wordDict:
#                 dp[i] = True
#                 break
#     print(dp[n])





'''
pleas refer :
https://songhuiming.github.io/pages/2018/03/18/leetcode-140-word-break-ii/
'''
def www(s,wordDic):
    mem = {}
    def dfs(s,wordDic):
        if s in mem:
            return mem[s]
        ans = []
        if s in wordDic:
            ans.append(s)
        for j in range(1,len(s)):
            right = s[j:]
            if right not in  wordDic:
                continue
            left = s[:j]
            left_ans = [x + ' ' + right for x in dfs(left,wordDic)]
            ans += left_ans
        mem[s] = ans
        return mem[s]
    return dfs(s,wordDic)
    # n = len(s)
    # dp = [''] * (n+1)
    # dp[0] = 'a'
    # for i in range(1,n+1):
    #     for j in range(i):
    #         sub_string = s[j:i]
    #         if dp[j] != ''  and sub_string in wordDic:
    #             for e in dp[j]:
    #                 dp[i] = e + ' ' + sub_string
    # print(dp[n])

s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
print(www(s,wordDict))
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]


















