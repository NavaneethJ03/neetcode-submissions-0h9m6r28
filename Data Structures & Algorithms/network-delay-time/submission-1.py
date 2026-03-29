class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u , v , w in times:
            graph[u].append([v , w])

        minHeap = [[0 , k]]
        visit = set()
        time = 0
        while minHeap:
            w1 , v1 = heapq.heappop(minHeap)
            if v1 in visit:
                continue

            visit.add(v1)
            time = w1

            for v2 , w2 in graph[v1]:
                if v2 not in visit:
                    heapq.heappush(minHeap , [w1 + w2 , v2])

        return time if len(visit) == n else -1
