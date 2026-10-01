class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, curr, t):
            if t == 0:
                res.append(curr.copy())
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                if candidates[j] > t:
                    break

                curr.append(candidates[j])
                dfs(j + 1, curr, t - candidates[j])
                curr.pop()

        dfs(0, [], target)
        return res