print()
'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''
import collections
def minWindow(S,T):
    t = tcount = collections.Counter(T)
    match_nums = len(T)
    left = 0
    count = 0
    res = []
    for i in range(1,len(S)):
        curr_s = S[i]
        if curr_s in t.keys():
            t[curr_s] -= 1
            if t[curr_s] >= 0:
                count += 1
        while count == match_nums:
            if S[left] not in t.keys():
                left +=1
            else:
                t[S[left]] += 1
                if t[S[left]] > 0:
                    count -= 1
                    res.append([left,i-left+1])
    index = len(S)
    ss = ''
    for e in res:
        left = e[0]
        if left < index:
            index = left
            ss = S[index:e[1]]
    print(ss)


S = "ADOBECODEBANC"
T = "ABC"
minWindow(S,T)



















