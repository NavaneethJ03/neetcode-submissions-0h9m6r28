class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        cycle , visit = set() , set()

        graph = {i : [] for i in range(n)}

        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node , parent):
            if node in cycle:
                return False 
            if node in visit:
                return True 

            cycle.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei , node):
                    return False

            cycle.remove(node)
            visit.add(node)
            return True

        dfs(0 , -1)
        if len(visit) == n:
            return True

        return False 
