# 27. Remove Element
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        input_nums = nums.copy()
        nums.clear()
        [nums.append(el) for el in input_nums if el != val]

        return len(nums)


solution = Solution()

print(solution.removeElement(nums=[3,2,2,3], val=3))  #  2   nums = [2,2,_,_]      
print(solution.removeElement(nums=[0,1,2,2,3,0,4,2], val=2))


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        input_nums = nums.copy()
        nums.clear()
        for el in input_nums:
            nums.append(el) if el != val else None

        return len(nums)


solution = Solution()

print(solution.removeElement(nums=[3,2,2,3], val=3))  #  2   nums = [2,2,_,_]      
print(solution.removeElement(nums=[0,1,2,2,3,0,4,2], val=2))


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        input_nums = nums.copy()
        nums.clear()
        nums.extend([el for el in input_nums if el != val])

        return len(nums)


solution = Solution()

print(solution.removeElement(nums=[3,2,2,3], val=3))  #  2   nums = [2,2,_,_]      
print(solution.removeElement(nums=[0,1,2,2,3,0,4,2], val=2))


class Solution:  # for val only from 0 to 9, not to 100
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_str = [str(el) for el in nums]
        input_nums = [int(el) for el in list(''.join(nums_str).replace(str(val), ''))]
        nums.clear()
        nums.extend(input_nums)

        return len(nums)


solution = Solution()

print(solution.removeElement(nums=[3,2,2,3], val=3))  #  2   nums = [2,2,_,_]      
print(solution.removeElement(nums=[0,1,2,2,3,0,4,2], val=2))
print(solution.removeElement(nums=[], val=2))


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for el in range(nums.count(val)):
            nums.remove(val)

        return len(nums)


solution = Solution()

# print(solution.removeElement(nums=[3,2,2,3], val=3))  #  2   nums = [2,2,_,_]      
print(solution.removeElement(nums=[0,1,2,2,3,0,4,2], val=2))  # 5
# print(solution.removeElement(nums=[], val=2))


'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
'''
'''
Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
'''