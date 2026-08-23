class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {i : [] for i in range(len(points))}
        for i in range(len(points)):
            x1 , y1 = points[i]
            for j in range(i + 1 ,len(points)):
                x2 , y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                graph[i].append([j , dist])
                graph[j].append([i , dist])


        visit = set()
        minHeap = [[0 , 0]]
        res = 0

        while len(visit) < len(points):
            cost , node = heapq.heappop(minHeap)
            if node in visit:
                continue
            res += cost 
            visit.add(node)

            for neiNode , neiCost in graph[node]:
                if neiNode not in visit:
                    heapq.heappush(minHeap , [neiCost , neiNode])

        return res

