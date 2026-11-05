class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = {}
        graph = {i : [] for i in range(numCourses)}
        for crs , pre in prerequisites:
            graph[crs].append(pre)

        def dfs(crs):
            if crs in visit:
                if visit[crs] == 1:
                    return True
                return False 

            visit[crs] = 0

            for prereq in graph[crs]:
                if not dfs(prereq):
                    return False 

            visit[crs] = 1 

            return True 

        for crs in range(numCourses):
            if not dfs(crs):
                return False 

        return True

            