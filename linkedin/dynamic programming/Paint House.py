'''
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
             Minimum cost: 2 + 5 + 3 = 10.
'''


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # def minCost(self, costs: 'List[List[int]]') -> 'int':
        red, blue, green = 0, 0, 0
        for r, b, g in costs:
            red, blue, green = min(blue, green) + r, min(red, green) + b, min(red, blue) + g

        return min(red, blue, green)

#         if len(costs) == 0:
#             return 0

#         dp = [0 for _ in range(len(costs))]

#         dp[0] = min(costs[0])
#         pre_coloer = costs[0].index(dp[0])

#         for i in range(1,len(costs)):
#             # red = costs[i][0]
#             # bule = costs[i][1]
#             # green = costs[i][2]
#             temp = costs[i]
#             temp.remove(costs[i][pre_coloer])
#             dp[i] = dp[i-1] + min(temp)
#             pre_coloer = costs[i].index(min(temp))
#             temp = None
#         return dp[-1]