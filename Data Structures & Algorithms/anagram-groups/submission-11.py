class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for s in strs:
            chrMap = [0] * 26 
            for c in s:
                chrMap[ord(c) - ord('a')] += 1
            anagram[tuple(chrMap)].append(s)

        return list(anagram.values())