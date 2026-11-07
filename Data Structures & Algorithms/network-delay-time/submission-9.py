class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = 0 
        graph = {i : [] for i in range(1 , n + 1)}

        for u , v , w in times:
            graph[u].append([v , w])
        
        minHeap = [[0 , k]]
        visit = set()

        while minHeap:
            w , node = heapq.heappop(minHeap)
            if node not in visit:
                visit.add(node)
                time = w
                for neiNode , neiWeight in graph[node]:
                    heapq.heappush(minHeap , [w + neiWeight , neiNode])

        return time if len(visit) == n else -1