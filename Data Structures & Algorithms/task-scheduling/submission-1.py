class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-v for v in count.values()]
        heapq.heapify(heap)
        q = deque()
        time = 0 
        while q or heap:
            time += 1 
            if heap:
                task = heapq.heappop(heap)
                task += 1 
                if task:
                    q.append([task , time + n])
                
            if q:
                if time >= q[0][1]:
                    task , t = q.popleft()
                    heapq.heappush(heap , task)

        return time 
        
