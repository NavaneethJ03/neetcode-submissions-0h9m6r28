class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}

        def dfs(i , isHold):
            if i >= len(prices):
                return 0 
            key = (i , isHold)
            if key in memo:
                return memo[key]
            
            memo[key] = dfs(i + 1 , isHold)
            if isHold:
                sell = prices[i] + dfs(i + 2 , False)
                memo[key] = max(memo[key] , sell)
            else:
                buy = -prices[i] + dfs(i + 1 , True)
                memo[key] = max(memo[key] , buy)

            return memo[key]

        return dfs(0 , False)