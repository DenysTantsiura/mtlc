# 1337. The K Weakest Rows in a Matrix
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        if len(mat) < k:
            k = len(mat)
        
        if k < 1:
            return None
        
        # full_map = {num:el.count(1) for num, el in enumerate(range(len(mat)))}
        ## invers_map = {full_map[num]:num for num in full_map} # --- corupted dulicates
        map_list = list(map(lambda x: x.count(1), mat))  # [2,4,1,2,5]
        result = []
        while k:
            k -= 1
            weakest_index = map_list.index(min(map_list))
            result.append(weakest_index)
            # map_list.pop(min(map_list))
            map_list[weakest_index] += 101

        return result


solution = Solution()

print(solution.kWeakestRows([[1,1,0,0,0],
                            [1,1,1,1,0],
                            [1,0,0,0,0],
                            [1,1,0,0,0],
                            [1,1,1,1,1]], 1))  # [2]


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        if len(mat) < k:
            k = len(mat)
        
        if k < 1:
            return None
        
        # full_map = {num:el.count(1) for num, el in enumerate(range(len(mat)))}
        full_map = {num:el.count(1) for num, el in enumerate(mat)}
        
        map_list = list(map(lambda x: x.count(1), mat))  # [2,4,1,2,5]
        map_list.sort()
        result = []
        for _ in range(k):
            for num, count1 in full_map.items():
                if map_list[0] ==count1:
                    result.append(num)
                    full_map.pop(num)
                    map_list.pop(0)
                    break

        return result
    
solution = Solution()

print(solution.kWeakestRows([[1,1,0,0,0],
                            [1,1,1,1,0],
                            [1,0,0,0,0],
                            [1,1,0,0,0],
                            [1,1,1,1,1]], 3))  # [2, 0, 3]


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        if len(mat) < k:
            k = len(mat)
        
        if k < 1:
            return None

        full_map = [(el.count(1), num) for num, el in enumerate(mat)]
        full_map.sort()

        return [el[1] for el in full_map[:k]]
    
    
solution = Solution()

print(solution.kWeakestRows([[1,1,0,0,0],
                            [1,1,1,1,0],
                            [1,0,0,0,0],
                            [1,1,0,0,0],
                            [1,1,1,1,1]], 3))  # [2, 0, 3]
