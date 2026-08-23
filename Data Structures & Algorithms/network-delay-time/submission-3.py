class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i : [] for i in range(1 , n + 1)}
        for u , v , w in times:
            graph[u].append([v , w])
        minHeap = [[0 , k]]
        visit = set()
        time = 0 
        while minHeap:
            t , node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            time = t 
            for v , w in graph[node]:
                if v not in visit:
                    heapq.heappush(minHeap , [w + time , v])
                    

        return time if len(visit) == n else -1