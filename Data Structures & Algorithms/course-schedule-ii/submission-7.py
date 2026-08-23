class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Kahn's Algo 

        graph = {i : [] for i in range(numCourses)}
        indeg = [0] * numCourses
        for c , p in prerequisites:
            graph[p].append(c)
            indeg[c] += 1 
         
        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        res = []
        while q:
            c = q.popleft()
            res.append(c)
            for p in graph[c]:
                indeg[p] -= 1
                if indeg[p] == 0:
                    q.append(p)

        return res if len(res) == numCourses else []