# 70. Climbing Stairs == Fibonacci
# 1 <= n <= 45
class Solution(object):
    def climbStairs(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 1

        for _ in range(n-1):
            a, b = b, a + b

        return b

[print(Solution().climbStairs(el)) for el in range(45)]
