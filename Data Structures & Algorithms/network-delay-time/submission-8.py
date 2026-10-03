class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i : [] for i in range(1 , n + 1)}
        for u , v , w in times:
            graph[u].append([v , w])
        visit = set()
        minHeap = [[0 , k]]
        time = 0 

        while minHeap:
            t , node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            time = t 
            for neiNode , neiCost in graph[node]:
                if neiNode not in visit:
                    heapq.heappush(minHeap , [neiCost + t , neiNode])

        return time if len(visit) == n else -1