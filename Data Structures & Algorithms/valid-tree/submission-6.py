class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i : [] for i in range(n)}
        visit = set()
        cycle = set()
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node , parent):
            if node in visit:
                return True
            if node in cycle:
                return False 

            cycle.add(node)
            for neiNode in graph[node]:
                if neiNode == parent:
                    continue
                if not dfs(neiNode , node):
                    return False 

            cycle.remove(node)
            visit.add(node)
            return True

        if dfs(0 , -1):
            return n == len(visit)
        return False


        