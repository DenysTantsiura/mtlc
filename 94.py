# 94. Binary Tree Inorder Traversal
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rez = []

        def step_next(self, root: Optional[TreeNode]):
            step_next(self, root.left) if root.left else None
            rez.append(root.val) if root else None
            step_next(self, root.right) if root.right else None

        if not root or (not root.left and not root.right):
            return rez if not root else [root.val]
        
        left, right = root.left, root.right

        step_next(self, root.left) if root.left else None
        rez.append(root.val)
        step_next(self, root.right) if root.right else None
        
        return rez


zero = TreeNode(val=1, right=TreeNode(val=3))


print(rez:=Solution().inorderTraversal(zero))
        
"""
Input: root = [1,null,2,3]
Output: [1,3,2]
"""

'''
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if node:
                dfs(node.left)
                res.append(node.val)
                dfs(node.right)
        
        dfs(root)

        return res
'''