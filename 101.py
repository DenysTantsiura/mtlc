
# https://leetcode.com/problemset/all/?status=NOT_STARTED&page=2
# 101. Symmetric Tree
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def isright(node_1: Optional[TreeNode], node_2: Optional[TreeNode]) -> bool:
        return True if (not node_1 and not node_2) or (node_1 and node_2 and node_1.val == node_2.val) else False
    
    @staticmethod
    def next_(node_ls: Optional[TreeNode], node_rs: Optional[TreeNode]):
        a = node_ls.left if node_ls else None
        b = node_rs.right if node_rs else None
        c = node_ls.right if node_ls else None
        d = node_rs.left if node_rs else None
        if not a and not b and not c and not c:
            return True

        if (not Solution.isright(a, b) 
            or not Solution.isright(c, d)):
            
            return False

        return (Solution.next_(a, b) 
                and Solution.next_(c, d))

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 
        
        rl = root.left
        rr = root.right
        if (rl is None and rr) or (rr is None and rl) or (rl and rr and rl.val != rr.val):
            return False
        
        return self.next_(rl, rr)

 
# print(rez:=Solution().isSymmetric(None)) 

# ex0 = TreeNode(val=0)

# print(rez:=Solution().isSymmetric(ex0))   

ex1 = TreeNode(val=1, right=TreeNode(val=3))

print(rez:=Solution().isSymmetric(ex1))             

# ex2 = TreeNode(val=1, left=TreeNode(val=3), right=TreeNode(val=3))

# print(rez:=Solution().isSymmetric(ex2))  

# ex3 = TreeNode(val=1, left=TreeNode(val=3, left=TreeNode(val=3), right=TreeNode(val=3)), right=TreeNode(val=3, left=TreeNode(val=3), right=TreeNode(val=3)))

# print(rez:=Solution().isSymmetric(ex3))  

# ex4 = TreeNode(val=1, left=TreeNode(val=3, left=TreeNode(val=3)), right=TreeNode(val=3, right=TreeNode(val=3)))

# print(rez:=Solution().isSymmetric(ex4))  

# ex5 = TreeNode(val=1, left=TreeNode(val=3, left=TreeNode(val=4), right=TreeNode(val=3)), right=TreeNode(val=3, left=TreeNode(val=4), right=TreeNode(val=3)))

# print(rez:=Solution().isSymmetric(ex5))  


"""
class Solution:
    def isright(self, nl, nr):
        if not nl and not nr:
            return True
        
        if not nl or not nr:
            return False
        
        return nl.val == nr.val and self.isright(nl.left, nr.right) and self.isright(nl.right, nr.left)


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.isright(root.left, root.right)

"""