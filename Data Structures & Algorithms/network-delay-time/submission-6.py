class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i : [] for i in range(1 , n + 1)}
        visit = set()
        minHeap = [[0 , k]]
        time = 0
        for u , v , t in times:
            graph[u].append([v , t])

        while minHeap:
            w , node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            time = w 
            for neiNode , neiWeight in graph[node]:
                if neiNode not in visit:
                    heapq.heappush(minHeap , [neiWeight + time , neiNode])

        return time if len(visit) == n else -1
