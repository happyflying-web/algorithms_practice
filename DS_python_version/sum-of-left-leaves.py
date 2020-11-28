# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
当需要用到父节点的信息时，需要用栈的数据结构来保存父节点的信息
'''
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        list_1=[]
        sum =0
        if root :
            list_1.append(root)
        while(len(list_1)!=0):
            temp=list_1.pop()
            if temp.left and temp.left.left is None \
                and temp.left.right is None:
                sum=sum+temp.left.val
            if temp.left:
                list_1.append(temp.left)
            if temp.right:
                list_1.append(temp.right)

        return sum


