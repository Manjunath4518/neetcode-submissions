class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for x in nums:
                if x in used:
                    continue
                used.add(x)
                curr.append(x)

                dfs(curr)

                curr.pop()
                used.remove(x)

        dfs([])
        return res