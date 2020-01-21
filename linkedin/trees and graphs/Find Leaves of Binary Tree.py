'''
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.



Example:

Input: [1,2,3,4,5]

          1
         / \
        2   3
       / \
      4   5

Output: [[4,5,3],[2],[1]]


Explanation:

1. Removing the leaves [4,5,3] would result in this tree:

          1
         /
        2


2. Now removing the leaf [2] would result in this tree:

          1


3. Now removing the leaf [1] would result in the empty tree:

          []
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:

        def getLevel(root, d):
            if not root:
                return 0
            left = getLevel(root.left, d)
            right = getLevel(root.right, d)
            level = 1 + max(left, right)
            d[level].append(root.val)
            return level

        d = collections.defaultdict(list)
        getLevel(root, d)
        res = []
        for k in sorted(d.keys()):
            res.append(d[k])
        return res

        # 可以理解为将高度一样的都存再一个list里面
        # 从下网上，最底层的高度为0
#         if root == None:
#             return -1
#         res = []
#         map_height = {}

#         def helper(root,map_height):
#             if root == None:
#                 return -1
#             height = max(helper(root.left,map_height),helper(root.right,map_height)) + 1
#             if height in map_height.keys():
#                 map_height[height].append(root.val)
#             else:
#                 map_height[height] = [root.val]
#             root.left = None
#             root.right = None
#         helper(root,map_height)
#         for key,value in map_height.items():
#             res.append(value)
#         return res

















