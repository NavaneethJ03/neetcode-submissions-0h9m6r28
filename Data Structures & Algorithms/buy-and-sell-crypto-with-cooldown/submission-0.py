class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # To solve this problem , we need to be aware of the current state what we are in , whether to buy or to sell , cooldown is common among all
        # The 3 states in this problem are cooldown , buy and sell 
        # isBuy -> True - Buy
        # isBuy -> False - Sell
        dp = {}

        def dfs(i , isBuy):
            if i >= len(prices):
                return 0 

            if (i , isBuy) in dp:
                return dp[(i , isBuy)]

            if isBuy:
                buy = dfs(i + 1 , not isBuy) - prices[i] # this gives out the max profit from this point afterwards
                cooldown = dfs(i + 1 , isBuy) # we do the cooldown operation in here and now we will take the best option by getting the max out of both 
                dp[(i , isBuy)] = max(buy , cooldown)
            else:
                sell = dfs(i + 2 , not isBuy) + prices[i]
                cooldown = dfs(i + 1 , isBuy)
                dp[(i , isBuy)] = max(sell , cooldown)

            return dp[(i , isBuy)]

        return dfs(0 , True )