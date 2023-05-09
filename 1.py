# 1. Two Sum
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        last_nums = list(map(lambda x: target - x, nums))

        for el in nums:
            a = nums.index(el)

            try:
                b = last_nums.index(el) if target / 2 != el / 1 else last_nums[a+1:].index(el) + a + 1
                if a == b:
                    continue
                
                result = [a, b]

                return result
            
            except:
                continue


solution = Solution()

print(solution.twoSum([3, 5, 6, 7], 9))  # [0, 2]
print(solution.twoSum([3, 2, 4], 6))  # [1, 2]
print(solution.twoSum([3, 3], 6))  # [0, 1]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        book = {}
        for i in range(len(nums)):
            if nums[i] in book: 
                
                return[book[nums[i]], i]
            
            book[target - nums[i]] = i


solution = Solution()

print(solution.twoSum([3, 5, 6, 7], 9))  # [0, 2]
print(solution.twoSum([3, 2, 4], 6))  # [1, 2]
print(solution.twoSum([3, 3], 6))  # [0, 1] 
