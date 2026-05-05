class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0 
        low = prices[0]
        for p in prices:
            profit = p - low 
            ans = max(ans , profit)
            if p < low:
                low = p 

        return ans 