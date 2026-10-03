class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        visit , cycle = set() , set()
        graph = {i : [] for i in range(numCourses)}
        for crs , pre in prereq:
            graph[crs].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False 

            if crs in visit:
                return True 

            cycle.add(crs)
            for pre in graph[crs]:
                if not dfs(pre):
                    return False 

            cycle.remove(crs)
            visit.add(crs)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False 

        return True