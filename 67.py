# 67. Add Binary
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        a, b = a[-1::-1], b[-1::-1]
        if len(a) < len(b):
            a += '0'*(len(b) - len(a))
        else:
            b += '0'*(len(a) - len(b))

        addition = 0

        for el in range(len(a)):
            if addition == 0:
                result += '0' if a[el] == b[el] else '1'
                addition = 1 if (int(a[el]) + int(b[el])) == 2 else 0
            elif (int(a[el]) + int(b[el])) == 1:
                result += '0'  #  result = f'{result}0'
                addition = 1
            else:
                result += '1'
                addition = 0 if a[el] == '0' else 1

        result += '1' if addition else '0'
        result = result[-1::-1]

        return result[result.find('1'):] if int(result) else '0'


solution = Solution()

print(solution.addBinary('1', '0'))  # 1, 0


"""
Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""