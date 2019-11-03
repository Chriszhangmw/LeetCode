'''
给定一个数组和一个数值，找出数组中的两个元素，使两个元素的和等于给定的值

'''

def get_num_under_sum(nums,value):
    nums.sort()
    for i in range(len(nums)):
        for j in range(len(nums)-1,-1,-1):
            if i < j:
                if nums[i] + nums[j] > value:
                    continue
                elif nums[i] + nums[j] < value:
                    break
                else:
                    print(str(nums[i]) + ' and ' + str(nums[j]))


def method1(nums,target):
    nums = sorted(nums)
    len1 = len(nums)
    res = []
    if len1 >= 2:
        low,high = 0,len1-1
        while low < high:
            if nums[low] + nums[high] == target:
                res.append((nums[low],nums[high]))
                low +=1
                high -= 1
            elif nums[low] + nums[high] > target:
                high -= 1
            else:
                low +=1
        print(res)

#hash table
def method2(nums,target):
    result = []
    for i,value in enumerate(nums):
        if (target - value) in nums[i+1:]:
            result.append((value,target-value))
    print(result)
    return result


def method3(nums,target):
    len1 = len(nums)
    res = []
    myres = []
    if len1 > 2:
        low,high = 0,len1-1
        while low < high:
            if nums[low] + nums[high] == target:
                res.append([nums[low],nums[high]])
                low +=1
                high -=1
            elif nums[low] + nums[high] > target:
                high-=1
            else:
                low +=1
        lentmp = len(res)
        if lentmp > 1:
            tmp = []
            for i in range(lentmp):
                tmp.append(res[i][0]*res[i][1])
            index = tmp.index(min(tmp))
            myres = res[index]
    print(myres)


def method4(nums,target):
    res = []
    min_value = 10000
    for i,value in enumerate(nums):
        if target-value in nums[i+1:]:

            if value * (target-value) < min_value:
                min_value = value * (target-value)
                res = [value,target-value]
    print(res)


def method5(nums,target):
    nums.sort()
    res = []
    for i in range(len(nums)-1):
        left,right = i+1,len(nums)-1
        while left<right:
            if nums[i] + nums[left] + nums[right] == target and (nums[i],nums[left],nums[right]) not in res:
                res.append((nums[i],nums[left],nums[right]))
                left+=1
                right-=1
            elif nums[i] + nums[left] + nums[right] > target:
                right-=1
            else:
                left+=1
    print(res)

def method6(nums,target):
    res = []
    for i,value in enumerate(nums):
        for j,value2 in enumerate(nums[i+1:]):
            if target-value2-value in nums[i+2:]:
                res.append((value,value2,target-value2-value))
    print(res)



nums = [1, 4, 3, 2, 6, 5]
value = 6
method6(nums,value)













