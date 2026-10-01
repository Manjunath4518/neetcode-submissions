
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = {}

        def solve(i, curr):
            if i == len(s):
                return ''.join(curr) in wordDict

            key = (i, ''.join(curr))

            if key in dp:
                return dp[key]

            curr.append(s[i])

            o = False
            if ''.join(curr) in wordDict:
                o = solve(i + 1, [])

            t = solve(i + 1, curr.copy())

            dp[key] = o or t

            return dp[key]

        return solve(0, [])

