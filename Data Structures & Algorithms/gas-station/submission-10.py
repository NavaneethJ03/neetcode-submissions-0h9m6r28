class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1 

        tank = shortage = 0 

        index = 0 

        for i in range(len(gas)):
            tank += gas[i]
            if tank >= cost[i]:
                tank -= cost[i]
            else:
                shortage = cost[i] - tank
                index = i + 1 
                tank = 0 

        if index == len(gas):
            return -1 

        return index