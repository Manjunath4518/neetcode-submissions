class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def solve(i):
            if i == 0:
                return 0

            if i < 0:
                return float('inf')

            if i in dp:
                return dp[i]

            res = float('inf')

            for coin in coins:
                res = min(res, 1 + solve(i - coin))

            dp[i] = res
            return dp[i]

        ans = solve(amount)

        return -1 if ans == float('inf') else ans