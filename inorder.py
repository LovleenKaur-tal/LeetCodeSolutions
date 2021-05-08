# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        l = []

        def func(node):
            if node == None:
                return
            func(node.left)
            l.append(node.val)
            func(node.right)

        func(root)
        return l
