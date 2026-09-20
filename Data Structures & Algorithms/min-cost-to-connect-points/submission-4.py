class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {i : [] for i in range(len(points))}
        visit = set()
        for i in range(len(points)):
            x1 , y1 = points[i][0] , points[i][1]
            for j in range(i + 1 , len(points)):
                x2 , y2 = points[j][0] , points[j][1]
                dist = abs(x2 - x1) + abs(y2 - y1)
                graph[i].append([j , dist])
                graph[j].append([i , dist])

        minHeap = [[0, 0]]
        res = 0 
        while len(visit) < len(points):
            cost , node = heapq.heappop(minHeap)
            if node in visit:
                continue 
            visit.add(node)
            res += cost 
            for neiNode , neiCost in graph[node]:
                if neiNode in visit:
                    continue
                heapq.heappush(minHeap , [neiCost , neiNode])
        return res
