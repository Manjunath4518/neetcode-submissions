class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        def dfs(m):
            if not m:
                return False

            if m.val == subRoot.val:
                if sameTree(m, subRoot):
                    return True

            return dfs(m.left) or dfs(m.right)

        return dfs(root)