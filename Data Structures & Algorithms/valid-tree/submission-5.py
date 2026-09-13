class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit , cycle = set() , set()
        graph = {i : [] for i in range(n)}
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)
        res = []
        def dfs(node , parent):
            if node in visit:
                return True
            if node in cycle:
                return False 

            cycle.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei , node):
                    return False 
            res.append(node)
            cycle.remove(node)
            visit.add(node)

            return True

        return dfs(0 , -1) and len(res) == n