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

import collections
def tool(A,k):
    left = 0
    res = 0
    cur = collections.defaultdict(int)
    for i in range(len(A)):
        temp = A[i]
        cur[temp] += 1
        while len(list(cur)) > k:

            cur[A[left]] -= 1
            if cur[A[left]] == 0:
                cur.pop(A[left])
            left += 1
        res += i - left + 1
    return res


def subarraysWithKDistinct(A,k):
    print(tool(A,k) - tool(A,k-1))

A = [1,2,1,2,3]
k = 2

subarraysWithKDistinct(A,k)














