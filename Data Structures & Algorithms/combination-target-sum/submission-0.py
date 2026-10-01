class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, t):
            if t == 0:
                res.append(curr.copy())
                return

            if i == len(nums) or t < 0:
                return

            dfs(i + 1, curr, t)

            curr.append(nums[i])
            dfs(i, curr, t - nums[i])
            curr.pop()

        dfs(0, [], target)
        return res