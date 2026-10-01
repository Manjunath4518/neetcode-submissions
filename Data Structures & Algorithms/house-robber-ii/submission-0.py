class Solution:
    def rob(self, nums: List[int]) -> int:

        def solve(l, r):
            dp = {}

            def dfs(i):
                if i > r:
                    return 0

                if i in dp:
                    return dp[i]

                t = nums[i] + dfs(i + 2)
                nt = dfs(i + 1)

                dp[i] = max(t, nt)
                return dp[i]

            return dfs(l)

        n = len(nums)

        if n == 1:
            return nums[0]

        return max(
            solve(0, n - 2),
            solve(1, n - 1)
        )