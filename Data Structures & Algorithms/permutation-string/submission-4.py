class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # s: frequency map for s1
        s = {}
        for c in s1:
            # Corrected: Use ord(c)-ord('a') as the key for s.get
            s[ord(c) - ord('a')] = 1 + s.get(ord(c) - ord('a'), 0)

        j = len(s1) # Length of the window

        for i in range(len(s2) - j + 1):
            h = {} # h: frequency map for the current window in s2
            window = s2[i : i + j]
            # print(window) # For debugging, uncomment if needed

            for c in window:
                # Corrected: Use ord(c)-ord('a') as the key for h.get
                h[ord(c) - ord('a')] = 1 + h.get(ord(c) - ord('a'), 0)

            if h == s:
                return True

        return False