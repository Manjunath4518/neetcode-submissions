class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {}

        def solve(i):
            if i <= 1:
                return i

            if i == 2:
                return 1
            if i in dp:
                return dp[i]

            dp[i] = solve(i-1) + solve(i-2) + solve(i-3)

            return dp[i]

        return solve(n)