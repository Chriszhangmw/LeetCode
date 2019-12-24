'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

def first(arr,low,high,x):
    if (high >= low):
        mid = low + (high - low)//2
        if ((mid == 0 or x > arr[mid -1]) and arr[mid] == x):
            return mid
        elif(x > arr[mid]):
            print(mid, high)
            return first(arr,(mid+1),high,x)
        else:
            return first(arr,low,mid-1,x)
    return -1


def last(arr,low,high,x,n):
    if(high >= low):
        mid = low + (high - low)//2
        print(arr[mid])
        if ((mid == n-1 or x < arr[mid + 1]) and arr[mid] == x):
            print(mid)
            return mid
        elif(x > arr[mid]):
            print(mid,high)
            return last(arr,(mid+1),high,x,n)
        else:
            return last(arr,low,(mid-1),x,n)
    return -1


def last2(arr, low, high, x, n):
    if (high >= low):
        mid = low + (high - low) // 2
        if ((mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x):
            return mid
        elif (x < arr[mid]):
            return last(arr, low, (mid - 1), x, n)
        else:
            return last(arr, (mid + 1), high, x, n)

    return -1



def first2(arr,x):
    left = 0
    right = len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if x == arr[mid] and x > arr[mid -1]:
            return mid
        elif x > arr[mid]:
            left = mid+1
        else:
            right = mid-1
    return -1
def second2(arr,x):
    left = 0
    right = len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if x == arr[mid] and x < arr[mid+1]:
            return mid
        elif x > arr[mid]:
            left = mid+1
        else:
            right = mid-1
    return -1





arr = [5,7,7,8,8,10]
n = len(arr)

x = 8
print(first2(arr,x))
print(second2(arr,x))
# print("First Occurrence = ",
#       first(arr, 0, n - 1, x))
# print("Last Occurrence = ",
#       last2(arr, 0, n - 1, x,n))









