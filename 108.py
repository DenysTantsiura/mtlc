# 108. Convert Sorted Array to Binary Search Tree
"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.

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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        ...


print(rez:=Solution().sortedArrayToBST([])) 