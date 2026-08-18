class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        visit = set()
        for c , r in prerequisites:
            preMap[c].append(r)

        def dfs(c):
            if c in visit:
                return False 

            if preMap[c] == []:
                return True

            visit.add(c)
            for p in preMap[c]:
                if not dfs(p):
                    return False 

            preMap[c] = []
            visit.remove(c)

            return True 

        for c in range(numCourses):
            if not dfs(c):
                return False 

        return True
