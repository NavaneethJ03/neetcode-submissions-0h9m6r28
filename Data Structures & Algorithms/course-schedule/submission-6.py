class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        visit = set()
        for c , p in prerequisites:
            preMap[c].append(p)

        def dfs(c):
            if c in visit:
                return False 

            if preMap[c] == []:
                return True 
            visit.add(c)
            for p in preMap[c]:
                if not dfs(p):
                    return False 

            visit.remove(c)
            preMap[c] = []
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False 

        return True
        