# 35. Search Insert Position
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        if target < nums[0] or target > nums[-1]:
            return 0 if target < nums[0] else len(nums)
        for el in range(1, len(nums)+1):
            if nums[el] > target and nums[el-1] < target:
                return el

solution = Solution()

print(solution.searchInsert(nums = [1,3,5,6], target = 5))  #  2 
print(solution.searchInsert(nums = [1,3,5,6], target = 2))  #  1
print(solution.searchInsert(nums = [1,3,5,6], target = 7))  #  4


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        nums.append(target)
        for el in range(len(nums)):
            if nums[el] > target:
                return el
            
        return el

solution = Solution()

print(solution.searchInsert(nums = [1,3,5,6], target = 5))  #  2 
print(solution.searchInsert(nums = [1,3,5,6], target = 2))  #  1
print(solution.searchInsert(nums = [1,3,5,6], target = 7))  #  4



class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        if target < nums[0] or target > nums[-1]:
            return 0 if target < nums[0] else len(nums)
        for el in range(len(nums)):
            if nums[el] > target:
                return el
            
        return el+1

solution = Solution()

print(solution.searchInsert(nums = [1,3,5,6], target = 5))  #  2 
print(solution.searchInsert(nums = [1,3,5,6], target = 2))  #  1
print(solution.searchInsert(nums = [1,3,5,6], target = 7))  #  4

"""
        for index, item in enumerate(nums):
            if item >= target:
                return index
            
        
        return len(nums)
"""
