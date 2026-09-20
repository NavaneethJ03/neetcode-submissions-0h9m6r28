class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}
        for crs , pre in prereq:
            graph[crs].append(pre)
        visit , cycle = set() , set()
    
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
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False 

        return True

