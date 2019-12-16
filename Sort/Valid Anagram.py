'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
'''


def method(s,l):
    a = [0]*26
    b = [0]*26
    for i in s:
        a[ord(i) - 97] +=1
    for j in l:
        b[ord(j) - 97] +=1
    return a == b

def method2(s,l):
    pass











