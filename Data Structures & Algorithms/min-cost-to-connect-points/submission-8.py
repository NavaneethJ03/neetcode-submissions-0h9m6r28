class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {i : [] for i in range(len(points))}
        for i in range(len(points)):
            x1 , y1 = map(int,points[i])
            for j in range(i + 1 , len(points)):
                x2 , y2 = map(int , points[j])
                dist = abs(x2 - x1) + abs(y2 - y1)
                graph[i].append([dist , j])
                graph[j].append([dist , i])

        cost = 0 
        visit = set()
        minHeap = [[0 , 0]]

        while len(visit) != len(points):
            w , node = heapq.heappop(minHeap)
            if node not in visit:
                visit.add(node)
                cost += w
                for neiDist , neiNode in graph[node]:
                    if neiNode not in visit:
                        heapq.heappush(minHeap , [neiDist , neiNode])

        return cost