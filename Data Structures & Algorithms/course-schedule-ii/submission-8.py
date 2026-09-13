class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i : [] for i in range(numCourses)}
        for c , p in prerequisites:
            graph[c].append(p)

        cycle , visit = set() , set()
        res = []
        def dfs(crs):
            if crs in visit:
                return True 

            if crs in cycle:
                return False 

            cycle.add(crs)
            for pre in graph[crs]:
                if not dfs(pre):
                    return False 
                
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)

            return True 

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res 