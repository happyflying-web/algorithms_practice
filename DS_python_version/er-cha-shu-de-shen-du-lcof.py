# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # n = 0
        def dfs(root):
            if root is None:
                return 0
            # if root.left or root.right:
            #     n=n+1
            if root and root.right is None and root.left is None:
                return 1
            else:
                return max(dfs(root.left)+1, dfs(root.right)+1)
        res=dfs(root)
        return res
