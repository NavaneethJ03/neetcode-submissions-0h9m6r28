class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)

        for s in strs:
            chrMap = [0] * 26
            for c in s:
                chrMap[ord(c) - ord('a')] += 1 
            anagramDict[tuple(chrMap)].append(s)

        return list(anagramDict.values())