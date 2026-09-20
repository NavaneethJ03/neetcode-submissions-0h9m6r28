class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = {i : [] for i in range(numCourses)}
        indeg = [0] * numCourses
        for crs , pre in prerequisites:
            graph[pre].append(crs)
            indeg[crs] += 1 

        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)

        while q:
            for _ in range(len(q)):
                crs = q.popleft()
                res.append(crs)
                for pre in graph[crs]:
                    indeg[pre] -= 1 
                    if indeg[pre] == 0:
                        q.append(pre)
                    
        return res if len(res) == numCourses else []