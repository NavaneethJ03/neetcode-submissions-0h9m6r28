class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charArr = [0] * 26
        ans = l = 0 
        for r in range(len(s)):
            charArr[ord(s[r]) - ord('A')] += 1 
            maxCount = max(charArr)
            while (r - l + 1) - maxCount > k:
                charArr[ord(s[l]) - ord('A')] -= 1 
                l += 1 

            ans = max(ans , (r - l + 1))
        return ans 