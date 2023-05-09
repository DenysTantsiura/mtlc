# 20. Valid Parentheses



class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        if len(s) % 2:
            return False
        
        result = {
                  '(': ')',
                  '{': '}',
                  '[': ']',
                  }
        
        if not result.get(s[0], None):
            return False
        
        stamp = s[0]

        for el in s[1:]:
            if el in result:
                stamp += el
            elif len(stamp) > 0 and el == result.get(stamp[-1], None):
                stamp = stamp[:-1]
            else:
                return False

        return True if stamp == '' else False


solution = Solution()

print(solution.isValid('([}}])'))  # -
print(solution.isValid('()'))  # -   
print(solution.isValid('(]'))  # -
print(solution.isValid('[](){}({})(])'))  # -
print(solution.isValid('[](){}{}'))  # +





class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        if len(s) % 2:
            return False
        
        result = {
                  '(': ')',
                  '{': '}',
                  '[': ']',
                  }
        
        if not result.get(s[0], None):
            return False
        
        stamp = [s[0]]

        for el in s[1:]:
            if el in result:
                stamp.append(el)
            elif len(stamp) > 0 and el == result.get(stamp[-1], None):
                stamp.pop()
            else:
                return False

        return True if not stamp else False


solution = Solution()

print(solution.isValid('([}}])'))  # -
print(solution.isValid('()'))  # -   
print(solution.isValid('(]'))  # -
print(solution.isValid('[](){}({})(])'))  # -
print(solution.isValid('[](){}{}'))  # +

