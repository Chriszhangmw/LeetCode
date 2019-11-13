'''
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
'''

def method(letter,k):
    left = 0
    right = len(letter)-1
    while left < right:
        mid = (left + right)/2
        if letter[mid] < k:
            left = mid +1
        else:
            if mid < 1 or (mid >= 1 and letter[mid-1] <= k):
                return letter[mid]
            else:
                right = mid -1
    return letter[0]
    # if k >= letter[-1]:
    #     return letter[0]
    # elif k < letter[0]:
    #     return letter[0]
    # else:









