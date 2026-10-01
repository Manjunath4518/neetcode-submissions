class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        def solve(path,used):
            if len(path) == len(nums):
                res.add(tuple(path))
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                path.append(nums[i])
                solve(path,used)

                path.pop()
                used[i] = False

        solve([],[False]*len(nums))
        ans = []
        for i in res:
            ans.append(list(i))
        return ans