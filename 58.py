# 58. Length of Last Word
class Solution(object):
    def lengthOfLastWord(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        return len(s.rstrip().split()[-1])


print(Solution().lengthOfLastWord(' Gerteyyye het    '))
