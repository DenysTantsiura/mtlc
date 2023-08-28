# 226. Invert Binary Tree
"""
https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.

"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or root.val is None:
            return None

        return TreeNode(
                        root.val, 
                        Solution.invertTree(self, root=root.right if root else None), 
                        Solution.invertTree(self, root=root.left if root else None)
                        )


a1 = TreeNode(1)
a2 = TreeNode(3)
a = TreeNode(2, a1, a2)

test = Solution().invertTree(root=a)
test1 = test.left.val
test2 = test.right.val
print(test1, test2)

a1 = TreeNode(1)
a2 = TreeNode(3)
a3 = TreeNode(6)
a4 = TreeNode(9)
a10 = TreeNode(2, a1, a2)
a20 = TreeNode(7, a3, a4)
a = TreeNode(4, a10, a20)

test = Solution().invertTree(root=a)
test10 = test.left.val
test20 = test.right.val
test1 = test.left.left.val
test2 = test.left.right.val
test3 = test.right.left.val
test4 = test.right.right.val
print(test.val, test10, test20, test1, test2, test3, test4)  # 4 7 2 9 6 3 1 
