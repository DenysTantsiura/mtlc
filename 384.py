# 384. Shuffle an Array
class Solution:
    from random import shuffle

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        new = self.nums[:]
        shuffle(new)
        return new

    def __repr__(self) -> List[int]:
        return 'null'

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
