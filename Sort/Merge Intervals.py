
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

#冒泡排序
def maopao(nums):
    hasChange = True
    for i in range(len(nums)):
        if hasChange == True:
            hasChange = False
            for j in range(len(nums)-i-1):
                if nums[j+1] < nums[j]:
                    tmp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = tmp
                    hasChange = True
    print(nums)

def charu(nums):
    for i in range(1,len(nums)):
        current = nums[i]
        j = i-1
        while j>=0 and nums[j] > current:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = current
    print(nums)


nums = [2,4,6,1,8,3,5,0]
charu(nums)

def method1(nums):
    hasChange = True
    for i in range(len(nums)):
        if hasChange == True:
            hasChange = False
            for j in range(len(nums)-i-1):
                if nums[j+1][0] < nums[j][0]:
                    tmp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = tmp
                    hasChange = True
    print('after sort :',nums)
    res = []
    for num in nums:
        if len(res) == 0:
            res.append(num)
        else:
            current_s = num[0]
            current_e = num[1]
            res_end = res[-1][1]
            if res_end < current_s:
                res.append(num)
            elif res_end > current_s:
                res[-1][1] = max(res_end,current_e)
            else:
                res[-1][1] = current_e
    print(res)


nums = [[1,4],[4,5]]
# method1(nums)






















