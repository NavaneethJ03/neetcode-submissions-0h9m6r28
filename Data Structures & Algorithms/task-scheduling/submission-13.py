class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        count = Counter(tasks)
        maxHeap = [-v for k , v in count.items()]
        q = deque()
        heapq.heapify(maxHeap)
        while q or maxHeap:
            time += 1 
            if maxHeap:
                task = heapq.heappop(maxHeap)
                task += 1 
                if task != 0:
                    q.append([task , time + n])
            if q:
                if time == q[0][1]:
                    task , t = q.popleft()
                    heapq.heappush(maxHeap , task)

        return time