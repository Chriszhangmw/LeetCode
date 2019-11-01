'''
题目描述: （挑了一个比较严谨的描述。问题描述严谨很重要，不然会影响解题思路）
一幢 100 层的大楼,给你两个鸡蛋. 如果在第 n 层扔下鸡蛋,鸡蛋不碎,那么从前 n-1 层扔鸡蛋都不碎.
这两只鸡蛋一模一样,不碎的话可以扔无数次. 已知鸡蛋在0层扔不会碎.
提出一个策略, 要保证能测出鸡蛋恰好不会碎的楼层, 并使此策略在最坏情况下所扔次数最少.
————————————————
版权声明：本文为CSDN博主「lonelyrains」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/lonelyrains/article/details/46428569
'''

class Solution:
    def superEggDrop(self):
        state = [[0] *37 for i in range(3)]
        for i in range(37):
            state[0][i] = 0
            state[1][i] = i

        for i in range(3):
            state[i][0] = 0
            state[i][1] = 1

        for i in range(2,37):
            for j in range(2,3):
                result = 10000
                for drop in range(1,i):
                    brek = state[j-1][drop-1]
                    unbrek = state[j][i-drop]
                    result = min(max(brek,unbrek) + 1,100000)
                state[j][i] = result
        print(result)

# a = Solution()
# print(a.superEggDrop())


def method(k,n):
    dp = [[0] * n for _ in range(k)]
    for i in range(k+1):
        dp[i][0] = 0
        dp[i][1] = 1
    for i in range(n+1):
        dp[0][i] = 0
        dp[1][i] = 1

    for egg in range(2,n):
        for floor in range(2,k):
            dp[egg][floor] = 100000
            for k in range(floor):
                dp[egg][floor] = min(1+max(dp[egg-1][floor-1],dp[egg][k-floor]),dp[egg][floor] )
    print(dp[egg][floor])


method(36,2)























