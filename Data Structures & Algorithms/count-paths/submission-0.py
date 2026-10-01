class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}

        def solve(i, j):
            if i == m - 1 and j == n - 1:
                return 1

            if i == m or j == n:
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            d = solve(i + 1, j)
            r = solve(i, j + 1)

            dp[(i, j)] = d + r
            return dp[(i, j)]

        return solve(0, 0)