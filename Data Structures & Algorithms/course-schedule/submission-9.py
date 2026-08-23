class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}
        visit = set()
        for c , r in prerequisites:
            graph[c].append(r)

        def dfs(c):
            if c in visit:
                return False 

            if graph[c] == []:
                return True 

            visit.add(c)

            for p in graph[c]:
                if not dfs(p):
                    return False 
            graph[c] = []
            visit.remove(c)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False 

        return True