'''

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6
'''
#
# def guess(num):
#     if num == 6:
#         return num
#     else:
#         pass
#
# def method(n):
#     left = 1
#     right = n
#     while left <= right:
#         mid = (left + right)//2
#         if guess(mid)==0:
#             pass

'''
n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.

'''



def method1(n):
    dp = [[0] * (n+1) for _ in range(n+1)]
    left = 1
    right = n
    return comm(dp,1,n)
def comm(dp,left,right):
    if left >= right:
        return 0
    if dp[left][right]:
        return dp[left][right]
    dp[left][right] = min(i + max(comm(dp,left,i-1),comm(dp,i+1,right)) for i in range(left,right+1))
    return dp[left][right]



















