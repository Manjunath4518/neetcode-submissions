class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = list(range(1, n + 1))
        res = []

        def dfs(i, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return

            if i == len(arr):
                return

            for j in range(i, len(arr)):
                curr.append(arr[j])
                dfs(j + 1, curr)
                curr.pop()

        dfs(0, [])
        return res