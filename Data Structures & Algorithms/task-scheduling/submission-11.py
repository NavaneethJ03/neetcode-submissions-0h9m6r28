class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        q = deque()
        maxHeap = [-v for k , v in count.items()]
        heapq.heapify(maxHeap)
        time = 0 
        while q or maxHeap:
            time += 1 
            if maxHeap:
                task = heapq.heappop(maxHeap)
                task += 1 
                if task != 0:
                    q.append([time + n , task])

            if q:
                if time >= q[0][0]:
                    t , task = q.popleft()
                    heapq.heappush(maxHeap , task)

        return time 