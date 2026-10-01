class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        res = 0
        l = 0

        for r in range(len(s)):

            while s[r] in seen:
                seen[s[l]] -= 1

                if seen[s[l]] == 0:
                    del seen[s[l]]

                l += 1

            seen[s[r]] = 1

            res = max(res, r - l + 1)

        return res