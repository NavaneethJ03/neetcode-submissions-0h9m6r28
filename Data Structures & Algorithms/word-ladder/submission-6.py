class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or endWord not in wordList:
            return 0

        graph = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = str(word[:i] + '*' + word[i+1:])
                graph[pattern].append(word)
        visit = set()
        visit.add(beginWord)
        q = deque([beginWord])
        ans = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return ans
                for i in range(len(word)):
                    pattern = str(word[:i] + '*' + word[i+1:])
                    for neiWord in graph[pattern]:
                        if neiWord not in visit:
                            q.append(neiWord)
                            visit.add(neiWord)

            ans += 1 

        return 0

                        