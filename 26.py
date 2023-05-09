# 26. Remove Duplicates from Sorted Array
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  # , nums
        
        if len(nums) == len(set(nums)):
            return len(nums)  # , nums
        
        result = []
        k = 0
        for el in nums.copy():
            if el not in result:
                result.append(el)
                k += 1
            else:
                nums.pop(k)    
                
        return k


# solution = Solution()
# nums = [0,0,1,1,1,2,2,3,3,4]
# print(solution.removeDuplicates(nums))  # 5, [0,1,2,3,4,_,_,_,_,_]
# print(nums)
# nums = [1,1,2]
# print(solution.removeDuplicates(nums))  # 5, [0,1,2,3,4,_,_,_,_,_]
# print(nums)

'''
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  # , nums
        
        if len(nums) == len(set(nums)):
            return len(nums)  # , nums
        
        result = []
        for el in nums.copy():
            if el not in result:
                result.append(el)

            else:
                nums.pop(len(result))    
                
        return len(nums)


# solution = Solution()
# nums = [0,0,1,1,1,2,2,3,3,4]
# print(solution.removeDuplicates(nums))  # 5, [0,1,2,3,4,_,_,_,_,_]
# print(nums)
# nums = [1,1,2]
# print(solution.removeDuplicates(nums))  # 5, [0,1,2,3,4,_,_,_,_,_]
# print(nums)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  # , nums
        
        if len(nums) == len(set(nums)):
            return len(nums)  # , nums
        
        steps = len(nums)

        slide = 0
        for __ in range(len(nums)-1):
            if nums[slide] == nums[slide+1]:
                nums.pop(slide+1)
            else:
                slide += 1

        return slide+1  # len(nums)


# solution = Solution()
# nums = [0,0,1,1,1,2,2,3,3,4]
# print(solution.removeDuplicates(nums))  # 5, [0,1,2,3,4,_,_,_,_,_]
# print(nums)
# nums = [1,1,2]
# print(solution.removeDuplicates(nums))  # 5, [0,1,2,3,4,_,_,_,_,_]
# print(nums)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        block = set(nums)
        k = len(block)
        if k == len(nums):
            return k
        nums.clear()

        [nums.append(i) for i in block]
        
        nums.sort()
        
        return k


# solution = Solution()

# nums = [0,0,1,1,1,2,2,3,3,4]
# print(solution.removeDuplicates(nums))  # 5, [0,1,2,3,4,_,_,_,_,_]
# print(nums)
# nums = [1,1,2]
# print(solution.removeDuplicates(nums))  # 5, [0,1,2,3,4,_,_,_,_,_]
# print(nums)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        block = set(nums)
        k = len(block)
        if k == len(nums):
            return k
        nums.clear()

        while k:
            nums.append(block.pop())
            k -= 1
        
        nums.sort()
        
        return len(nums)


solution = Solution()

nums = [0,0,1,1,1,2,2,3,3,4]
print(solution.removeDuplicates(nums))  # 5, [0,1,2,3,4,_,_,_,_,_]
print(nums)
nums = [1,1,2]
print(solution.removeDuplicates(nums))  # 5, [0,1,2,3,4,_,_,_,_,_]
print(nums)


"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current_el = 0
        while current_el < len(nums) - 1:
            if nums[current_el] == nums[current_el+1]:
                nums.pop(current_el)

            else:
                current_el += 1

        return len(nums)
"""
