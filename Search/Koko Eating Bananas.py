'''
Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  The guards have gone and will come back in H hours.

Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.

Return the minimum integer K such that she can eat all the bananas within H hours.



Example 1:

Input: piles = [3,6,7,11], H = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], H = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], H = 6
Output: 23
'''



def method1(nums,hours):
    minSpeed = 1
    maxSpeed = max(nums)
    value = minSpeed + (maxSpeed - minSpeed)//2
    time = 0
    while time < hours:
        for num in nums:
           time += num//value + 1
        value -=1
    return value

print(method1([3,6,7,11],8))



def method2(nums,hours):
    minspeed = 1
    maxspeed = max(nums)
    while minspeed <= maxspeed:
        value = minspeed + (maxspeed - minspeed)//2
        hour = 0
        for num in nums:
            hour += num//value + 1
        if hour <= hours:
            maxspeed -=1
        else:
            minspeed +=1
    return minspeed

print(method2([30,11,23,4,20],6))



