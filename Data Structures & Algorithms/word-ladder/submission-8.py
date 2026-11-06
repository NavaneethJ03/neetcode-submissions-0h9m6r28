class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        wordList.append(beginWord)
        if endWord not in wordList:
            return 0 
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                graph[pattern].append(word)


        q = deque([beginWord])
        visit = set()
        ans = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return ans
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in graph[pattern]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)

            ans += 1 

        return 0
