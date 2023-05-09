# 9. Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        test1 = str(x)
        if test1 in test1[::-1]:

            return True
        
        return False


solution = Solution()

print(solution.isPalindrome(121))  # +


import math as m


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x <= 9:
            return True

        len_x = int(m.log(x, 10)) + 1
        for step in range(1, len_x - 1 if len_x > 2 else len_x):
           
            right_digit = (x % (10**step) - x % (10**(step-1))) // 10**(step-1)

            left_digit = (x // 10**(len_x - 1*step)) % 10

            if right_digit != left_digit:
                return False

        return True


solution = Solution()

print(solution.isPalindrome(121))  # +
print(solution.isPalindrome(999))  # +
print(solution.isPalindrome(53635))  # +
print(solution.isPalindrome(22))  # +
print(solution.isPalindrome(21))  # -
print(solution.isPalindrome(2112012))  # -
print(solution.isPalindrome(2882))  # +

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x[::-1] == x
    