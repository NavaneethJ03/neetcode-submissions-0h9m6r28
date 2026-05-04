class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)
        for word in strs:
            idx = [0] * 26
            for c in word:
                idx[ord(c) - ord('a')] += 1 
            anagramDict[tuple(idx)].append(word)

        return list(anagramDict.values())
