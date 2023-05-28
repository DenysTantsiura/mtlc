# 88. Merge Sorted Array
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1 = nums1[:m]
        [nums1.pop() for _ in range(len(nums1)-m)]
        nums2 = nums2[:n]
        nums1.extend(nums2)
        nums1.sort()
        

nums1 = [1,2,3,0,0,0]
print(rez:=Solution().merge(nums1 = nums1, m = 3, nums2 = [2,5,6], n = 3))
print(nums1)
