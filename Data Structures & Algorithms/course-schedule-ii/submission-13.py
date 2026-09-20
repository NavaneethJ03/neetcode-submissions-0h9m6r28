class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit , cycle = set() , set()
        graph = {i : [] for i in range(numCourses)}
        for crs , pre in prerequisites:
            graph[crs].append(pre)
        res = []
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
            res.append(crs)
            return True 

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
        # res = []
        # graph = {i : [] for i in range(numCourses)}
        # indeg = [0] * numCourses
        # for crs , pre in prerequisites:
        #     graph[pre].append(crs)
        #     indeg[crs] += 1 

        # q = deque()
        # for i in range(numCourses):
        #     if indeg[i] == 0:
        #         q.append(i)

        # while q:
        #     for _ in range(len(q)):
        #         crs = q.popleft()
        #         res.append(crs)
        #         for pre in graph[crs]:
        #             indeg[pre] -= 1 
        #             if indeg[pre] == 0:
        #                 q.append(pre)
                    
        # return res if len(res) == numCourses else []