'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
'''


def quick_sort(nums):
    if len(nums)< 2:
        return nums
    v = nums[0]
    left = [num for num in nums if num<v]
    right = [num for num in nums if num>v]
    left = quick_sort(left)
    right = quick_sort(right)
    res = []
    res += left
    res.append(v)
    res  +=right
    print(res)
    return res


nums = [3,1,4,2]
quick_sort(nums)






class test:
    def method2(self,root,k):
        self.count = 0
        self.res = 0
        def middle(root):
            if self.count < k:
                if root.left:
                    middle(root.left)
                self.count +=1
                if self.count == k:
                    self.res = root.val
                    return
                if root.right:
                    middle(root.right)
        if root:
            middle(root)
        return self.res



class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        res = 0
        while 1 :
            while root :
                stack.append(root)
                root = root.left
            if not stack : break
            root = stack.pop()
            k -= 1
            if k == 0 : return root.val
            root = root.right
        return 0




