class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # to solve this problem , first we gotta create the pattern graph and then match the pattern accordingly 

        if endWord not in wordList:
            return 0 

        res = 1
        visit = set([beginWord])
        graph = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1:]
                graph[pattern].append(word)

        q = deque([beginWord])
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res 
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j + 1:]
                    for neiWord in graph[pattern]:
                        if neiWord not in visit:
                            q.append(neiWord)
                            visit.add(neiWord)
            res += 1 
        
        
        return 0
            