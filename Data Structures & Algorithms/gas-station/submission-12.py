class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        tank = 0
        start = 0
        for i in range(len(gas)):
            tank += gas[i]
            if tank < cost[i]:
                tank = 0 
                start = i + 1
                continue 
            else:
                tank -= cost[i]

        return start
