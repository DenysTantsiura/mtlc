# next 104 !!!!!
# 104. Maximum Depth of Binary Tree
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    count = 0
    step = 2
    
    def insight(self, n):
        # self.count += 1
        if n is None:
            return
        
        if n.left or n.right:
            # self.count += 1
            l = self.insight(n.left)
            r = self.insight(n.right)
            self.count -= self.step - 1
            self.step *= 2 if r or l else 1
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            self.count += 1
            self.insight(root)

        return self.count


print(rez:=Solution().maxDepth(None)) 

ex0 = TreeNode(val=0)

print(rez:=Solution().maxDepth(ex0))   

ex1 = TreeNode(val=1, right=TreeNode(val=3))

print(rez:=Solution().maxDepth(ex1))             

ex2 = TreeNode(val=1, left=TreeNode(val=3), right=TreeNode(val=3))

print(rez:=Solution().maxDepth(ex2))  

ex3 = TreeNode(val=1, left=TreeNode(val=3, left=TreeNode(val=3), right=TreeNode(val=3)), right=TreeNode(val=3, left=TreeNode(val=3), right=TreeNode(val=3)))

print(rez:=Solution().maxDepth(ex3))  

ex4 = TreeNode(val=1, left=TreeNode(val=3, left=TreeNode(val=3)), right=TreeNode(val=3, right=TreeNode(val=3)))

print(rez:=Solution().maxDepth(ex4))  

ex5 = TreeNode(val=1, left=TreeNode(val=3, left=TreeNode(val=4), right=TreeNode(val=3)), right=TreeNode(val=3, left=TreeNode(val=4), right=TreeNode(val=3)))

print(rez:=Solution().maxDepth(ex5))  

ex6 = TreeNode(val=1, 
               left=TreeNode(val=3, 
                             left=TreeNode(val=4)), 
                right=TreeNode(val=4, 
                                right=TreeNode(val=3)))

print(rez:=Solution().maxDepth(ex6))  
