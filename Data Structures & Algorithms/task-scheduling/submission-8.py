class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0 
        count = Counter(tasks)
        maxHeap = [-v for v in count.values()]
        heapq.heapify(maxHeap)
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                task = heapq.heappop(maxHeap)
                task += 1 
                if task:
                    q.append([time + n , task])

            if q and q[0][0] <= time:
                t , task = q.popleft()
                heapq.heappush(maxHeap , task)

        return time 


