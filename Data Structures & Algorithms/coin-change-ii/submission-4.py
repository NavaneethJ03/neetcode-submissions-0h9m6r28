class Solution:
    def change(self, x: int, coins: List[int]) -> int:
        dp = [[0] * (x + 1) for _ in range(len(coins) + 1)]

        # for r in range(len(dp)):
        #     dp[r][0] = 1  # this because , we can make a value 0 in 1 way
        dp[0][0] = 1 
        for i in range(len(coins)): # -> coins 
            for j in range(x + 1): # -> amount 
                k = i + 1
                a = j - coins[i]
                top = dp[k - 1][j] 
                rem = dp[k][a] if a >= 0 else 0 
                dp[k][j] = top + rem

        return dp[-1][-1]



    