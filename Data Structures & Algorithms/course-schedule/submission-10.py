class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit , cycle = set() , set()

        graph = {i:[] for i in range(numCourses)}
        for p , c in prerequisites:
            graph[c].append(p)
        

        def dfs(crs):
            if crs in visit:
                return True

            if crs in cycle:
                return False 
            cycle.add(crs)
            for prereq in graph[crs]:
                if not dfs(prereq):
                    return False 
            cycle.remove(crs)
            visit.add(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False 

        return True