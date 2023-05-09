# 14. Longest Common Prefix
class Solution(object):
    def longestCommonPrefix(self, strs: list) -> str:
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        strs_len = [len(el) for el in strs]
        min_str = strs[strs_len.index(min(strs_len))]
        for num, el in enumerate(min_str):
            for word in strs:
                if word[num] != el:
                    return result
                
            result += el

        return result


solution = Solution()

print(solution.longestCommonPrefix(['flower','flow','flight']))  # fl
print(solution.longestCommonPrefix(['dog','racecar','car']))  # ''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        if len(strs) == 0:
            return result
        
        for num, el in enumerate(strs[0]):
            for word in strs[1:]:
                try:
                    if word[num] != el:
                        return result
                except:
                    return result
                
            result += el    

        return result


solution = Solution()

print(solution.longestCommonPrefix(['flower','flow','flight']))  # fl
print(solution.longestCommonPrefix(['dog','racecar','car']))  # ''



class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        
        str_len = list(map(lambda x: len(x), strs))
        min_word = strs[str_len.index(min(str_len))]

        for nel in range(len(min_word)+1, 0, -1):
            if all([word.startswith(min_word[:nel]) for word in strs]):
                return min_word[:nel]
            
        return ''


solution = Solution()

print(solution.longestCommonPrefix(['flower','flow','flight']))  # fl
print(solution.longestCommonPrefix(['dog','racecar','car']))  # ''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        for nel in range(len(strs[0])+1, 0, -1):
            if all([word.startswith(strs[0][:nel]) for word in strs[1:]]):
                return strs[0][:nel]
            
        return ''


solution = Solution()

print(solution.longestCommonPrefix(['flower','flow','flight']))  # fl
print(solution.longestCommonPrefix(['dog','racecar','car']))  # ''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        strs.sort(key=lambda x: len(x))
        print(strs)
        for nel in range(len(strs[0])+1, 0, -1):
            if all([word.startswith(strs[0][:nel]) for word in strs[1:]]):
                return strs[0][:nel]
            
        return ''


solution = Solution()

print(solution.longestCommonPrefix(['flower', 'fliffffffffff', 'flow','flight']))  # fl
print(solution.longestCommonPrefix(['dog','racecar','car']))  # ''
