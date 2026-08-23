class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visit = set()
        graph = {i : [] for i in range(1 , n + 1)}
        for u , v , t in times:
            graph[u].append([v , t])
        minHeap = [[0 , k]]
        time = 0 
        q = deque()
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


            

