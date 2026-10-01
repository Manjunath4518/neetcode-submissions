class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = float('-inf')

        def dfs(n):
            nonlocal res

            if not n:
                return 0

            l = max(0, dfs(n.left))
            r = max(0, dfs(n.right))

            res = max(res, n.val + l + r)

            return n.val + max(l, r)

        dfs(root)
        return res