# 110. Balanced Binary Tree
"""
https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is 
height-balanced.

?...
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        ...


print(rez:=Solution().isBalanced(None)) 

tree1 = TreeNode(0)
...
print(rez:=Solution().isBalanced(None)) 
