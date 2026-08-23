class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Kahn's Algo 

        graph = {i : [] for i in range(numCourses)}
        cycle , visit = set() , set()
        for c , r in prerequisites:
            graph[c].append(r)
        res = []
        def dfs(c):
            if c in cycle:
                return False 
            if c in visit:
                return True
            cycle.add(c)
            for p in graph[c]:
                if not dfs(p):
                    return False 
            visit.add(c)
            res.append(c)
            cycle.remove(c)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return res if len(res) == numCourses else []