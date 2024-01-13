class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = math.inf
        ans = 0
        for price in prices:
            profit = price - buy
            ans = max(ans, profit)
            buy = min(buy, price)
        return ans