# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def binaryTreePaths(self, root: TreeNode):
        def search(root: TreeNode, path: str, paths: []):
            if root:
                path = path + str(root.val)
                if root.left is None and root.right is None:
                    paths.append(path)
                else:
                    path=path+'->'
                    search(root.left, path, paths)
                    search(root.right, path, paths)

            return paths

        path = ""
        paths = []
        res = search(root, path, paths)
        return res
