class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        for task , pre in prerequisites:
            preMap[task].append(pre)

        visit = set()

        def dfs(i):
            if i in visit:
                return False 

            if preMap[i] == []:
                return True 

            visit.add(i)
            for p in preMap[i]:
                if not dfs(p):
                    return False 

            visit.remove(i)
            preMap[i] = []
            return True 

        for c in range(numCourses):
            if not dfs(c):
                return False 

        return True
            