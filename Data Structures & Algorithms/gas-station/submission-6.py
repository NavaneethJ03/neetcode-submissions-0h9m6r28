class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        tank = shortage = startIdx = 0
        for i in range(len(gas)):
            tank += gas[i]
            if tank >= cost[i]:
                tank -= cost[i]
            else:
                shortage = cost[i] - tank
                startIdx = i + 1
                tank = 0 

        return startIdx
        