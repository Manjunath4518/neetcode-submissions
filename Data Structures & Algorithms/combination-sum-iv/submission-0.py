class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        def solve(i, t):
            if t == 0:
                return 1

            if t < 0 or i >= len(nums):
                return 0
            if (i,t) in dp:
                return dp[(i,t)]                
            take = solve(0, t - nums[i])

        
            not_take = solve(i + 1, t)
            dp[(i,t)] = take+not_take

            return take + not_take

        return solve(0, target)