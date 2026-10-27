class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0 
        low = prices[0]
        for p in prices:
            profit = p - low 
            low = min(low , p)
            ans = max(ans , profit)

        return ans