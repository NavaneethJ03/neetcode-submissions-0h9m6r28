class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) 
        dp[0] = 0 # set the base case 

        for a in range(1 , amount + 1):
            for c in coins:
                if a >= c:
                    dp[a] = min(dp[a] , dp[a - c] + 1)
        # check for condition where the sum cannot be formed 
        return dp[amount] if dp[amount] != amount + 1 else -1