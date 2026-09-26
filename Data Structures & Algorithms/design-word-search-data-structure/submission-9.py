class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root 
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.isWord = True

    def search(self, word: str) -> bool:
        
        def dfs(i , node):
            cur = node
            for j in range(i , len(word)):
                if word[j] == '.':
                    for neiNode in cur.children.values():
                        if dfs(j + 1 , neiNode):
                            return True
                    return False
                else:
                    if word[j] not in cur.children:
                        return False 
                    cur = cur.children[word[j]]

            return cur.isWord
        return dfs(0 , self.root)

        
