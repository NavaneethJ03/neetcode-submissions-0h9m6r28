class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False 
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        res , visit = set() , set()
        # add all the words to the trie
        for w in words:
            curr = root 
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.isWord = True 
        rows , cols = len(board) , len(board[0])
        def dfs(r , c , node , word):
            if not(0 <= r < rows) or not(0 <= c < cols) or (r , c) in visit or board[r][c] not in node.children:
                return 

            visit.add((r , c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.isWord:
                res.add(word)

            dfs(r+1 , c , node , word)
            dfs(r-1 , c , node , word)
            dfs(r , c+1 , node , word)
            dfs(r , c-1 , node , word)
            visit.remove((r , c))

        for r in range(rows):
            for c in range(cols):
                dfs(r , c , root , "")

        return list(res)


