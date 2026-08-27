class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(day , hold):
            if day >= len(prices):
                return 0 

            key = (day , hold)

            if key in memo:
                return memo[key]

            cooldown = dfs(day + 1 , hold)

            if hold:
                sell = dfs(day + 2 , not hold) + prices[day]
                memo[key] = max(sell , cooldown)
            else:
                buy = dfs(day + 1 , not hold) - prices[day]
                memo[key] = max(buy , cooldown)

            return memo[key]

        return dfs(0 , False)
