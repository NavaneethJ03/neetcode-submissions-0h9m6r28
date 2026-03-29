class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u , v , time in times:
            graph[u].append([v , time])

        minHeap = [[0 , k]]
        visit = set()
        time = 0 
        
        while minHeap:
            weight , node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            time = weight

            for nei , weight2 in graph[node]:
                if nei not in visit:
                    heapq.heappush(minHeap , [weight2 + weight, nei])


        return time if len(visit) == n else -1
