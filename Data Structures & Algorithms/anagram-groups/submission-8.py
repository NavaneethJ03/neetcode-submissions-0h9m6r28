class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for s in strs:
            charArr = [0] * 26 
            for c in s:
                charArr[ord(c) - ord('a')] += 1 

            if tuple(charArr) not in hmap:
                hmap[tuple(charArr)] = []

            hmap[tuple(charArr)].append(s)

        return list(hmap.values())
            
            