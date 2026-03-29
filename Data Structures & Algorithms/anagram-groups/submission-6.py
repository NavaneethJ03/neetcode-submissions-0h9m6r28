class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hmap = defaultdict(list)
        for s in strs:
            charArr = [0] * 26 
            for c in s:
                charArr[ord(c) - ord('a')] += 1 

            hmap[tuple(charArr)].append(s)



        return list(hmap.values())

