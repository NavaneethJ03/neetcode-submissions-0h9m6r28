class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c:set() for word in words for c in word}

        for i in range(1 , len(words)):
            minLen = min(len(words[i-1]) , len(words[i]))
            if len(words[i - 1]) > len(words[i]) and words[i-1][:minLen] == words[i][:minLen]:
                return ""
            for j in range(minLen):
                if words[i-1][j] != words[i][j]:
                    graph[words[i-1][j]].add(words[i][j])
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

        for node in graph:
            if dfs(node):
                return ""

        return "".join(res[::-1])