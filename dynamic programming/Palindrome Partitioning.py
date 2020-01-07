'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''

#DFS method   https://www.youtube.com/watch?v=uIMzNr0ROi8
def isPali(s):
    return s == s[::-1]


def method(s,path,res):
    if s == '':
        res.append(path)
        return
    for i in range(1,len(s)+1):
        curr_s = s[:i]
        if isPali(curr_s):
            method(s[i:],path+s[:i],res)



def main(s):
    res = []
    method(s,[],res)


#DP

def dynamic_programming(s):
    m = len(s)
    if m == 0:
        return []
    def isP(i,j):
        while i<j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def solve(i):
        ans = []
        if i == m-1:
            return [[s[i]]]
        j = i
        while j < m:
            if isP(i,j):
                tmp = solve(j + 1)
                if len(tmp) == 0:
                    ans.append([s[i:j + 1]])
                else:
                    for k in tmp:
                        ans.append([s[i:j +1]] + k)
            j += 1
        return ans
    return solve(0)



'''
132. Palindrome Partitioning II
Hard

808

27

Add to List

Share
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''



class A:
    def isP(self,s):
        return s == s[::-1]

    def method(self,s):
        res = []
        path = 0
        self.helper(s,path,res)
        print(min(res)-1)
    def helper(self,s,path,res):
        if s == '':
            res.append(path)
            return
        for i in range(1,len(s) + 1):
            if self.isP(s[:i]):
                self.helper(s[i:],path + 1,res)

s = 'aab'
a = A()
a.method(s)


def method(s):
    n = len(s)
    dp = [i-1 for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(i):
            print(s[j:i])
            if s[j:i] == s[j:i][::-1]:
                dp[i] = min(dp[i],dp[j] + 1)
    print(dp[-1])

