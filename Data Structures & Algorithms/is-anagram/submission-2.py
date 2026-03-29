class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = Counter(s)
        s2 = Counter(t)
        if s1 == s2:
            return True
        return False