class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chararr = [0] * 26
        ans = 0
        l = 0 
        for r in range(len(s)):
            chararr[ord(s[r]) - ord('A')] += 1 
            maxx = max(chararr)
            while ((r - l + 1) - maxx > k):
                chararr[ord(s[l]) - ord('A')] -= 1 
                l += 1

            ans = max(ans , r - l + 1)

        return ans

