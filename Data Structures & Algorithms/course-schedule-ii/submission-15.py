class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i : [] for i in range(numCourses)}
        indeg = [0] * numCourses

        for crs , pre in prerequisites:
            graph[pre].append(crs)
            indeg[crs] += 1 

        q = deque()
        for i in range(len(indeg)):
            if indeg[i] == 0:
                q.append(i)
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nei in graph[node]:
                indeg[nei] -= 1 
                if indeg[nei] == 0:
                    q.append(nei)

        return res if len(res) == numCourses else []