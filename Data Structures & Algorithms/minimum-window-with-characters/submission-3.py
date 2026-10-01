from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = Counter(t)
        have = {}

        required = len(need)
        formed = 0

        l = 0
        ans = ""
        min_len = float('inf')

        for r in range(len(s)):

           
            c = s[r]
            have[c] = have.get(c, 0) + 1

            if c in need and have[c] == need[c]:
                formed += 1

           
            while formed == required:

               
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    ans = s[l:r + 1]

                
                c = s[l]
                have[c] -= 1

                if c in need and have[c] < need[c]:
                    formed -= 1

                l += 1

        return ans