# 1342. Number of Steps to Reduce a Number to Zero
class Solution:
    def numberOfSteps(self, num: int) -> int:
        # return [el for el in range(num, 0, -1)][-1]
        result = 0
        while num:
            if num % 2 == 0:
                num /= 2

            else:
                num -= 1
            result +=1

        return result


solution = Solution()

print(solution.numberOfSteps(99789))  # 14->6


class Solution:
    def numberOfSteps(self, num: int) -> int:
        result = 0
        while num:
            num = num // 2 if not (num % 2) else num - 1
            result +=1

        return result


solution = Solution()

print(solution.numberOfSteps(99789))  # 25
# print(solution.numberOfSteps(14))  # 6
# print(solution.numberOfSteps(8))  # 4
# print(solution.numberOfSteps(123))  # 12
# print(solution.numberOfSteps(8))  # 4
# print(solution.numberOfSteps(9))  # 4
# print(solution.numberOfSteps(10))  # 4

'''
Example 1:

Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.
Example 2:

Input: num = 8
Output: 4
Explanation: 
Step 1) 8 is even; divide by 2 and obtain 4. 
Step 2) 4 is even; divide by 2 and obtain 2. 
Step 3) 2 is even; divide by 2 and obtain 1. 
Step 4) 1 is odd; subtract 1 and obtain 0.
Example 3:

Input: num = 123
Output: 12
'''

# import math as m


# class Solution:
#     def numberOfSteps(self, num: int) -> int:
#         result = 0
#         nnum = 0
#         for el in range(int(m.log2(10**6)) + int(pow(10**6, 0.5)) + 3):
#             if nnum >= num or nnum+1 >= num:
#                 return result if nnum+1 > num else result-1
            
#             if nnum % 2 == 0:
#                 nnum += 1
#             else:
#                 nnum *= 2

#             result += 1

#         return result


# solution = Solution()

# print(solution.numberOfSteps(14))  # 6
# print(solution.numberOfSteps(8))  # 4
# print(solution.numberOfSteps(123))  # 12   99789
# print(solution.numberOfSteps(99789))  # 25

# # 0 <= num <= 10^6
# int(m.log2(10**6)) + int(pow(10**6, 0.5)) + 2
