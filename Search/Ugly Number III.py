'''
Write a program to find the n-th ugly number.

Ugly numbers are positive integers which are divisible by a or b or c.



Example 1:

Input: n = 3, a = 2, b = 3, c = 5
Output: 4
Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
Example 2:

Input: n = 4, a = 2, b = 3, c = 4
Output: 6
Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.
Example 3:

Input: n = 5, a = 2, b = 11, c = 13
Output: 10
Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
Example 4:

Input: n = 1000000000, a = 2, b = 217983653, c = 336916467
Output: 1999999984
'''

def method(n,a,b,c):
    k = 0
    while k < 20:
        res = []
        res.append(a)
        while a < b:
            a += a
            if a <= b:
                res.append(a)
            else:
                res.append(b)
                break
        while b < c:
            b += b
            if b < c:
                res.append(b)
            else:
                res.append(c)
                break
        a +=a
        b +=b
        c +=c
        k +=1
    print(res[n])
'''
dp = [1] * n
        index2, index3, index5 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(2 * dp[index2], 3 * dp[index3], 5 * dp[index5])
            if dp[i] == 2 * dp[index2]: index2 += 1
            if dp[i] == 3 * dp[index3]: index3 += 1
            if dp[i] == 5 * dp[index5]: index5 += 1
        return dp[n - 1]
'''

n = 5
a = 2
b = 11
c = 13

method(n,a,b,c)






