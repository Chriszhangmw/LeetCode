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
def method(s,t):
    left,cnt,minLen = 0,0,100
    index = 0
    tcount = collections.Counter(t)
    for i in range(len(s)):
        tmp = s[i]
        if tmp not in tcount.keys():
            continue
        else:
            tcount[tmp] -= 1
            if tcount[tmp] == 0:
                cnt += 1
            while cnt == len(t):
                if (i-left + 1) < minLen:
                    minLen = i-left + 1
                    index = left
                de_c = s[left]
                left += 1
                if de_c in tcount.keys():
                    tcount[de_c] += 1
                    if tcount[de_c] == 1:
                        cnt -=1
                else:
                    continue
    print(minLen)
    if minLen == float('inf') :
        print('hh')
    else:
        print(s[index:index + minLen])

s = "ADOBECODEBANC"
t = "ABC"

method(s,t)




    # left = 0
    # res = ''
    # curr = ''
    # for i in range(len(s)):
    #     curr = curr + s[i]
    #     if len(curr) > len(t):







