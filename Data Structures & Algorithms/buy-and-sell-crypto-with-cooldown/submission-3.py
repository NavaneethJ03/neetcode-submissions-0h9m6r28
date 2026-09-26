class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i , ishold):
            if i >= len(prices):
                return 0 
            key = (i , ishold)
            if key in memo:
                return memo[key]

            skip = dfs(i + 1 , ishold)

            if ishold:
                sell = prices[i] + dfs(i + 2 , False)
                memo[key] = max(sell , skip)
            else:
                buy = -prices[i] + dfs(i + 1 , True)
                memo[key] = max(buy , skip)

            return memo[key]

        return dfs(0 , False)
            