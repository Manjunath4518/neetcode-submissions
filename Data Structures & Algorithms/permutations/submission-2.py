class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def solve(path,used):
            if len(path) == len(used):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                path.append(nums[i])
                solve(path,used)
                used[i] = False
                path.pop()

        solve([],[False]*len(nums))
        return res