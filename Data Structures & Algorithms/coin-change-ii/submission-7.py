class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        for r in range(len(dp)):
            dp[r][0] = 1 

        for r in range(len(coins)):
            for c in range(1 , amount + 1):
                coin = coins[r]
                k = r + 1
                top = dp[k-1][c]
                left = dp[k][c - coin] if c - coin >= 0 else 0
                dp[k][c] = top + left
        return dp[-1][-1] if dp[-1][-1] != amount + 1 else 0