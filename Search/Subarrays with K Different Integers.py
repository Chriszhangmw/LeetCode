'''

Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.



Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
Example 2:

Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
'''


def subarraysWithKDistinct(A,k):
    from collections import deque
    left = 0
    res = []
    curr = []
    for i in range(len(A)):
        e = A[i]
        curr.append(e)
        if len(list(set(curr))) == k:
            res.append(curr)
            if len(curr) == k:
                continue
            else:
                while len(list(set(curr.pop(A[left])))) == k:
                    res.append(curr)
                    left += 1
    print(res)
    print(len(res))
A = [1,2,1,2,3]
k = 2

subarraysWithKDistinct(A,k)














