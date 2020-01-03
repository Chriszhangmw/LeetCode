'''

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

'''


def getMaximum(nums):
    sum = 0
    max = 0
    for num in nums:
        sum += num
        if sum>max:
            max = sum
        if sum<0:
            sum = 0
    return max



def method2(nums,n):
    maxV = 0
    return maxArray(nums,0,n-1,maxV)

def maxArray(nums,left,right,maxV):
    if left > right:
        return 0
    mid = (left+right)//2
    lamx = maxArray(nums,left,mid-1,maxV)
    rmax = maxArray(nums,mid+1,right,maxV)
    maxV = max(maxV,lamx)
    maxV = max(maxV,rmax)
    sum = 0
    mlmax=0
    for i in range(mid-1,left,-1):
        sum +=nums[i]
        if sum>mlmax:
            mlmax = sum

    sum = 0
    mrmax = 0
    for j in range(mid+1,right):
        sum +=nums[j]
        if sum > mrmax:
            mrmax = sum
    maxV = max(maxV,mlmax + mrmax + nums[mid])

    return maxV



def second_time(a):
    dp = [0] * len(a)
    if len(a) == 1:
        return a[0]
    dp[0] = a[0]
    for i in range(len(a)):
        if dp[i-1] < 0:
            dp[i] = a[i]
        else:
            dp[i] = dp[i-1] + a[i]
    return max(dp)





#可以考虑用双指针
def shuangzhizhen(a):
    left = 0
    res = 0
    for i in range(len(a)):
        res += a[i]
        if a[i] > 0:
            tmp = []
            tmp.append(res)
            while left < i:
#滑动窗口不行，因为每次减去哪个e可能是负的，减了反而变大，明显不合理，因为res一直累加的原因，反正这个题用滑动窗口是不合适的
                tmp.append(res - a[left])
                left += 1
            res = max(tmp)
    print(res)



a = [-2,1,-3,4,-1,2,1,-5,4]
print(shuangzhizhen(a))
# b = method2(a,9)
# print(b)



