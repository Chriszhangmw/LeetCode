print(
    222222
)

'''

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def method(root,depth):
    def help_(root,depth):
        for node in root:
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            if node.left:
                method(node.left,depth+1)
            if node.right:
                method(node.right,depth+1)

    res = []
    if root == []:
        return res
    depth = 0
    help_(root,depth)


















class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []  # store all the answers
        if not root:
            return levels

        def helper(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels











