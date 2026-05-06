class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-v for v in count.values()]
        heapq.heapify(heap)

        time = 0 
        q = deque()

        while heap or q:
            time += 1 
            if heap:
                task = heapq.heappop(heap)
                task += 1 
                if task:
                    q.append([task , time + n])

            if q:
                if q[0][1] <= time:
                    task , t = q.popleft()
                    heapq.heappush(heap ,task)


        return time 
        