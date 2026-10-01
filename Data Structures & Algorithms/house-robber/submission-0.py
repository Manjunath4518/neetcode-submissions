class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def solve(i):
            if i >= len(nums):
                return 0

            if i in dp:
                return dp[i]

            t = nums[i] + solve(i + 2)
            nt = solve(i + 1)

            dp[i] = max(t, nt)

            return dp[i]

        return solve(0)