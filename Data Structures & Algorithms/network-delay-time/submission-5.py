class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i : [] for i in range(1 , n + 1)}
        for u , v , t in times:
            graph[u].append([t , v]) 
        
        time = 0
        visit = set()
        minHeap = [[0 , k]]
        while minHeap:
            t , node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            time = t
            for weight , neiNode in graph[node]:
                if neiNode not in visit:
                    heapq.heappush(minHeap , [t + weight , neiNode])

        return time if len(visit) == n else -1

