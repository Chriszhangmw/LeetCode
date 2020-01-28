'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # 配套视频讲解https://www.youtube.com/watch?v=zyskis1Gw0c

        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]

            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]

            return store_index

        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:  # If the list contains only one element,
                return nums[left]  # return that element

            # select a random pivot_index between
            pivot_index = random.randint(left, right)

            # find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest
        return select(0, len(nums) - 1, len(nums) - k)

        # 掌握quick sort得方法

#         res = []

#         def juge(nums,a,time):
#             nums.remove(a)
#             if a in nums:
#                 juge(nums,a,time+1)
#             return time

#         def sort_nums(nums):
#             if len(nums)==1:
#                 return nums
#             a = nums[0]
#             left = [e in nums if e < a]
#             right = [e in nums if e > a]
#             left = sort_nums(left)
#             right = sort_nums(right)
#             res = []
#             res+=left
#             res.append(a)
#             res+=right


#         # [5,5,4]  这个方法如果用priority que可以解决，至少Java里很简单
#         from queue import PriorityQueue
#         a = PriorityQueue()
#         for i in range(len(nums)):
#             if len(a)<k:


#             else:

#                 if nums[i] > a[-1]:
#                     a.pop()
#                     a.appendleft(nums[i])
#         return a[-1]

