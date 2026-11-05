class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visit = set()
        graph = {i : [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for crs , pre in prerequisites:
            graph[pre].append(crs)
            indegree[crs] += 1 

        q = deque([crs for crs in range(numCourses) if indegree[crs] == 0])

        while q:
            crs = q.popleft()
            if crs not in visit:
                visit.add(crs)
                res.append(crs)
                for nei in graph[crs]:
                    indegree[nei] -= 1 
                    if indegree[nei] == 0:
                        q.append(nei)

        return res if len(res) == numCourses else []