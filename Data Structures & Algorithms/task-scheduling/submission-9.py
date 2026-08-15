class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        time = 0 
        q = deque()
        maxHeap = [-v for v in count.values()]
        heapq.heapify(maxHeap)
        while maxHeap or q:
            time += 1
            if maxHeap:
                task = heapq.heappop(maxHeap)
                task += 1 
                if task:
                    q.append([task , time + n])

            if q and q[0][1] <= time:
                task , t = q.popleft()
                heapq.heappush(maxHeap , task)

        return time



