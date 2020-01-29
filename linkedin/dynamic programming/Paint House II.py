'''
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5;
             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.
Follow up:
Could you solve it in O(nk) runtime?
'''


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0

        dp = [0 for _ in range(len(costs))]

        dp[0] = min(costs[0])
        first_list = costs[0]
        min_val = min(costs[0])
        pre_color_index = first_list.index(min_val)

        for i in range(1, len(costs)):
            temp_list = costs[i]
            temp = costs[i]
            same_color = temp_list[pre_color_index]
            temp_list = temp_list.remove(same_color)
            min_value = min(temp_list)
            pre_color_index = temp.index(min_value)

            dp[i] = dp[i - 1] + min_value

            # temp = None
            # temp_list = None
        return dp[-1]