class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        for r in range(len(dp)):
            dp[r][0] = 1

        for r in range(1 , len(dp)):
            for c in range(amount + 1):
                idx = r - 1 
                coin = coins[idx]

                top = dp[idx][c]
                left = dp[r][c - coin] if c - coin >= 0 else 0 

                dp[r][c] = top + left 


        return dp[-1][-1]