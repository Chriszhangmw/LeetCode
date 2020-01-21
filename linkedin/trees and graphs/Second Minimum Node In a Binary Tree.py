'''
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

Input:
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.


Example 2:

Input:
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:

        self.min = float('inf')
        self.second_min = float('inf')

        def dfs(root):
            if root.val < self.min:
                self.second_min = self.min
                self.min = root.val
            elif root.val < self.second_min and root.val != self.min:
                self.second_min = root.val
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

        if root:
            dfs(root)
        #         samllest = float('inf')
        #         second = float('inf')
        #         def helper(root,samllest,second):
        #             if root.val < smallest:
        #                 second = samllest
        #                 smallest = root.val
        #             elif root.val > smallest and root.val < second:
        #                 second = root.val
        #             if root.left:
        #                 helper(root.left,samllest,second)
        #                 helper(root.right,samllest,second)

        #         helper(root,samllest,second)
        if self.second_min == float('inf'):
            return -1
        else:
            return self.second_min








