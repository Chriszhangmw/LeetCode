'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

class Node():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def second(s,e):
    if s > e :
        return [None]
    res = []
    for curr_root in range(s,e+1):
        left = second(s,curr_root-1)
        right = second(curr_root+1,e)

        for e in left:
            for r in right:
                root = Node(curr_root)
                root.left = e
                root.right = r
                res.append(root)
    return res





























class TreeNode():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def generateTree(n):
    if n==0:return []
    return helper(1,n)

def helper(begin,end):
    if begin > end:
        return [None]
    if begin == end:
        return [TreeNode(begin)]
    res = []
    for i in range(begin,end+1):
        tmp = []
        left = helper(begin,i-1)
        right = helper(i+1,end)
        for m in left:
            for n in right:
                root = TreeNode(i)
                root.left=m
                root.right = n
                res.append(root)
    return res








