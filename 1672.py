# 1672. Richest Customer Wealth
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(wealth) for wealth in accounts])
