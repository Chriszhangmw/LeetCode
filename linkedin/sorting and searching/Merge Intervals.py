'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda k: k[0])
        res = []
        for i in intervals:
            if res and res[-1][1] >= i[0]:
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append(i)
        return res

        # if len(intervals) == 1:
        #     return intervals
        # for i in range(len(intervals)):
        #     curr_list = intervals[i]
        #     if (i+1) < len(intervals):
        #         next_list = intervals[i+1]
        #         if curr_list[1] >= next_list[0] and curr_list[1] <= next_list[1]:
        #             curr_list[1] = next_list[1]
        #             intervals.remove(next_list)
        #         elif curr_list[1] >= next_list[0] and curr_list[1] > next_list[1]:
        #             intervals.remove(next_list)
        # return intervals
