from collections import defaultdict , deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 
        wordList.append(beginWord)
        adjList = defaultdict(list)
        for word in wordList: # Creating the pattern list 
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 : ]
                adjList[pattern].append(word)
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1 
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res 
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in adjList[pattern]:
                        if neiWord not in visit:
                            q.append(neiWord)
                            visit.add(neiWord)
            res += 1 

        return 0 
        