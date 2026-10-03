class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c : set() for w in words for c in w}

        for i in range(1 , len(words)):
            w1 = words[i-1]
            w2 = words[i]
            minLen = min(len(w1) , len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
            
        visit = {}
        res = []
        def dfs(node):
            if node in visit:
                return visit[node]

            visit[node] = True
            for neiNode in graph[node]:
                if dfs(neiNode):
                    return True 
            visit[node] = False 
            res.append(node)
            return False 

        for c in graph:
            if dfs(c):
                return ""

        return "".join(res[::-1])