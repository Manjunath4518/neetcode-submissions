class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = []

        for i in range(n):
            st = ''

            for j in range(i, n):
                st += s[j]

                if st == st[::-1]:
                    res.append(st)

        return max(res, key=len)