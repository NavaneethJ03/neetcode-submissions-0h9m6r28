class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        for r in range(len(dp)): # this is to set the base case of zero sum to one 
            dp[r][0] = 1 

        for r , coin in enumerate(coins):
            for c in range(1 , amount + 1):
                cur_row = r + 1 
                top = dp[cur_row - 1][c]
                rem = dp[cur_row][c - coin] if c - coin >= 0 else 0
                dp[cur_row][c] = top + rem

        return dp[-1][-1]

            
        