class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # here we have to reach the top most above the stairs 
        dp = [0] * (len(cost) + 1) # hence we take it as len(cost) + 1
        # we can start from position 0 and 1 hence the cost is 0 for those and we start from 2 
        n = len(cost)
        for i in range(2 , n+1):
            # here is the main recurrance relation where we minimize the cost of 
            # taking stairs that is we break the problems into sub problems and then 
            # compute using the dp array where 
            dp[i] = min(cost[i-1] + dp[i-1] , dp[i-2] + cost[i-2])

        return dp[n]
        