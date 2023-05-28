# 69. Sqrt(x)
# do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
class Solution(object):
    def mySqrt(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """
        delta = x // (2 * (len(str(x)))) or 1

        a = (len(str(x)) // 2) * delta
        if a * a == x:
            return a
        
        while a * a > x:
            a -= (delta // 2) if delta >=2 else 1

        while a * a < x and delta:
            a += delta
            if a * a == x:
                return a 
            
            if a * a > x:
                a -= delta
                delta //= 2
             
        return a


print(Solution().mySqrt(25))

[print(f'{el} -> {Solution().mySqrt(el)}') for el in range(999, 1026)]
