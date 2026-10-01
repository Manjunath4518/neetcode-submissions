class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, curr, t):
            if t == 0:
                res.append(curr[:])
                return

            if i == len(candidates) or t < 0:
                return

            j = i + 1
            while j < len(candidates) and candidates[i] == candidates[j]:
                j += 1

           
            dfs(j, curr, t)

            
            curr.append(candidates[i])
            dfs(i + 1, curr, t - candidates[i])
            curr.pop()

        dfs(0, [], target)
        return res