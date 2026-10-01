class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}

        def solve(i):
            if i <= 1:
                return 0

            if i in dp:
                return dp[i]

            dp[i] = min(
                cost[i - 1] + solve(i - 1),
                cost[i - 2] + solve(i - 2)
            )

            return dp[i]

        return solve(len(cost))