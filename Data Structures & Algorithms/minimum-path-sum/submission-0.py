class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        m = len(grid)
        n = len(grid[0])

        def solve(i, j):
            
            if i == m or j == n:
                return float('inf')

            if i == m - 1 and j == n - 1:
                return grid[i][j]

            if (i, j) in dp:
                return dp[(i, j)]

            d = solve(i + 1, j)
            r = solve(i, j + 1)

            dp[(i, j)] = grid[i][j] + min(d, r)

            return dp[(i, j)]

        return solve(0, 0)