# 66. Plus One
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for num in range(-1, -len(digits)-1, -1):
            if digits[num] > 9:  # == 10
                if -len(digits) == num:
                    digits = [0] + digits
                digits[num-1] += 1
                # digits[num] %= 10
                digits[num] = 0
                continue

            return digits
        
        return digits


solution = Solution()

print(solution.plusOne([9]))  # 1, 0
print(solution.plusOne([4, 3, 2, 2]))  # 4, 3, 2, 3
print(solution.plusOne([1, 9]))  # 2, 0
print(solution.plusOne([8, 9, 9]))  # 9, 0, 0
print(solution.plusOne([1]))  # 2
print(solution.plusOne([4, 9, 9, 9, 9]))  # 5, 0, 0, 0, 0
print(solution.plusOne([9, 9, 9, 9]))  # 1, 0, 0, 0, 0


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(el) for el in digits]
        return [int(el) for el in list(str(int(''.join(digits))+1))]
       

solution = Solution()

print(solution.plusOne([9]))  # 1, 0
print(solution.plusOne([4, 3, 2, 2]))  # 4, 3, 2, 3
print(solution.plusOne([1, 9]))  # 2, 0
print(solution.plusOne([8, 9, 9]))  # 9, 0, 0
print(solution.plusOne([1]))  # 2
print(solution.plusOne([4, 9, 9, 9, 9]))  # 5, 0, 0, 0, 0
print(solution.plusOne([9, 9, 9, 9]))  # 1, 0, 0, 0, 0
