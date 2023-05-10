# 28. Find the Index of the First Occurrence in a String
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


solution = Solution()

print(solution.strStr(haystack="sadbutsad", needle="sad"))  #   
print(solution.strStr(haystack="leetcode", needle="leeto"))  # 

"""
if needle in haystack:
    return haystack.index(needle)
else:
    return -1
"""
