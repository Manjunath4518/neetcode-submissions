class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def solve(i, a):
            if a == amount:
                return 0

            if a > amount or i == len(coins):
                return float('inf')

            if (i, a) in dp:
                return dp[(i, a)]

            take = 1 + solve(i, a + coins[i])
            skip = solve(i + 1, a)

            dp[(i, a)] = min(take, skip)
            return dp[(i, a)]

        ans = solve(0, 0)

        return -1 if ans == float('inf') else ans