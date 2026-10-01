# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(n, mx):
            if not n:
                return 0

            if n.val >= mx:
                return 1 + dfs(n.left, n.val) + dfs(n.right, n.val)

            return dfs(n.left, mx) + dfs(n.right, mx)

        return dfs(root, float('-inf'))