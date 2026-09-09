class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i , isHold):
            if i >= len(prices):
                return 0 
            if (i , isHold) in memo:
                return memo[(i , isHold)]
            skip = dfs(i + 1 , isHold)
            if isHold:
                sell = prices[i] + dfs(i + 2 , False)
                memo[(i , isHold)] = max(skip , sell)

            else:
                buy = -prices[i] + dfs(i + 1 , True)
                memo[(i , isHold)] = max(skip , buy)

            return memo[(i , isHold)]

        return dfs(0 , False) 
