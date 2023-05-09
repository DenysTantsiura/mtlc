# 383. Ransom Note
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        blocks_rn = [el for el in ransomNote]
        for el in blocks_rn:
            if el in magazine:
                magazine = magazine.replace(el, '_', 1)
            else:
                return False
        return True
