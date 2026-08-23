class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        rank = [1] * (n + 1)
        parent = [i for i in range(n + 1)]

        def find(node):
            p = parent[node]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p 

            
            # if node != parent[node]:
            #     parent[node] = find(parent[node])
            # return parent[node]

        def union(n1 , n2):
            p1 , p2 = find(n1) , find(n2)
            if p1 == p2: # meaning we have a cycle in here 
                return False 
            
            if rank[p1] > rank[p2]:
                # meaning that the node p1 is the parent of the node p2
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True 

        for n1 , n2 in edges:
            if not union(n1 , n2):
                return [n1 , n2]

