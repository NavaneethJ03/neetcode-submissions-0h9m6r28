class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1  # meaning there's not enough gas

        start = 0
        tank = 0

        for i in range(len(gas)):
            tank += gas[i]
            if tank < cost[i]:  # cannot start from this point
                # Then update the start idx and reset the tank
                start = i + 1
                tank = 0
                continue

            else:
                tank -= cost[i]

        return start
