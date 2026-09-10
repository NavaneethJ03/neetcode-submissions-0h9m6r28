class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # ans = 0 
        # low = prices[0]
        # for p in prices:
        #     profit = p - low 
        #     ans = max(ans , profit)
        #     low = min(low , p)

        # return ans
        dp = {}

        def dfs(i , hold , limit):
            if i == len(prices) or limit == 0:
                return 0 
            if (i , hold , limit) in dp:
                return dp[(i , hold , limit)]

            skip = dfs(i + 1 , hold, limit)
            if hold:
                sell = prices[i] + dfs(i + 1 , False , limit - 1)
                dp[(i , hold , limit)] = max(skip , sell)
            else:
                buy = -prices[i] + dfs(i + 1 , True , limit)
                dp[(i , hold , limit)] = max(skip , buy)

            return dp[(i , hold , limit)]

        return dfs(0 , False , 1)