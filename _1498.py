# -1498. Number of Subsequences That Satisfy the Given Sum Condition
'''
Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
1 <= target <= 10^6
'''
from typing import List


def fact(number: int):
    return number*fact(number-1) if number - 1 > 0 else 1


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        result = 0
        for num1, el in enumerate(nums):
            for num2, sel in enumerate(nums[num1:]):
                if el + sel <= target:
                    result += 1
                    result += num2*2-1 if num2 > 2 else 1 if num2 > 1 else 0
                    # print(f'[{nums[num1:num2+num1+1]}]')

        return result
        

solution = Solution()

print(solution.numSubseq([3, 5, 6, 7], 9))  # 4
print(solution.numSubseq([3, 3, 6, 8], 10))  # 6
print(solution.numSubseq([2, 3, 3, 4, 6, 7], 12))  # 61
print(solution.numSubseq([2, 4, 6, 7], 9))  # 11???
print(solution.numSubseq([5,2,4,1,7,6,8], 16))  # 127? not 103
