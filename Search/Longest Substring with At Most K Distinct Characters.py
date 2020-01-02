'''
Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.
'''

import collections
def method(s,k):
    scount = collections.Counter(s)
    s1 = {}
    tt = 1
    for key,value in scount.items():
        if tt <= k:
            s1[key] = value

            tt += 1
    print(s1)
    left = 0
    cnt = 0
    maxL = 0
    start = 0
    for i in range(len(s)):
        tmp = s[i]
        if tmp not in s1.keys():
            continue
        else:
            s1[tmp] -= 1
            if s1[tmp] == 0:
                cnt += 1
            while cnt == k:
                if (i - left + 1) > maxL:
                    maxL = i - left + 1
                    start = left
                de_c = s[left]
                left += 1
                if de_c in s1.keys():
                    s1[de_c] += 1
                    if s1[de_c] == 1:
                        cnt -= 1
                else:
                    continue
    print(maxL)
    print(s[start:start + maxL])



s = "eceba"
k = 2
method(s,k)






