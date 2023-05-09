# 13. Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        r = rezult = 0
        sm = symbol_map = {
                        'I': 1,
                        'V': 5,
                        'X': 10,
                        'L': 50,
                        'C': 100,
                        'D': 500,
                        'M': 1000
                        }
        s = s[::-1]
        r = sm[s[0]]
        b = before_element = sm[s[0]]
        for el in s[1:]:
            if sm[el] >= b:
                r += sm[el]
            elif sm[el] < b:
                r -= sm[el]
            b = sm[el]
        return r
