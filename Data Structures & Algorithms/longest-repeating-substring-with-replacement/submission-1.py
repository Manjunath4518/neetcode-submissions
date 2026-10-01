class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0
        mx = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1

            mx = max(mx,count[s[r]])

            while (r-l+1) - mx > k:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]

                l += 1

            res = max(res,r-l+1)

        return res