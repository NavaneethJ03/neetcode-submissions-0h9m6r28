class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []
        preMap = {i : [] for i in range(numCourses)}
        visit , cycle = set() , set()
        for c , p in prerequisites:
            preMap[c].append(p)

        def dfs(course):
            if course in cycle:
                return False 

            if course in visit:
                return True 

            cycle.add(course)
            for p in preMap[course]:
                if not dfs(p):
                    return False 

            cycle.remove(course)
            output.append(course)
            visit.add(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return output if len(output) == numCourses else []