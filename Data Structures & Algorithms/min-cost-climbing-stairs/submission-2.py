class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        n = len(cost)
        for i in range(2 , n+1):
            dp[i] = min(cost[i-1] + dp[i-1] , dp[i-2] + cost[i-2])

        return dp[n]
        