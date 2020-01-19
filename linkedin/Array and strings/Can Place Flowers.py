'''

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
'''


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        length = len(flowerbed)
        if length < 0 or length > 20000:
            return False
        max_num = length // 2 + 1

        if n == 0:
            return True
        if n > max_num:
            return False

        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # 解法1：
        # 首末加0是为了便于处理边界
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        # 只遍历原始的数据，不考虑后来加上的
        i = 1
        while i < len(flowerbed) - 1:
            if flowerbed[i] == 0:
                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    n -= 1
                    # 如果当前这个放置了，那么它后面的一个一定不能再放置
                    i += 1
            i += 1
        return n <= 0






