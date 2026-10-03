class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {i : [] for i in range(len(points))}
        for i in range(len(points)):
            xi , yi = points[i]
            for j in range(i + 1 , len(points)):
                xj , yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                graph[i].append([j , dist])
                graph[j].append([i , dist])

        minHeap = [[0 , 0]]
        visit = set()
        cost = 0 
        while len(visit) != len(points):
            w , node = heapq.heappop(minHeap)
            if node in visit:
                continue
            cost += w 
            visit.add(node)
            for neiNode , neiCost in graph[node]:
                if neiNode not in visit:
                    heapq.heappush(minHeap , [neiCost , neiNode])

        return cost

