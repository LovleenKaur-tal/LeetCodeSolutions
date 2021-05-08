# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        sum_total = 0

        def func(sum_total, node):
            if node:
                sum_total = sum_total + node.val
            if not node:
                return False
            if (node.left == None and node.right == None and sum_total == targetSum):
                return True
            return func(sum_total, node.left) or func(sum_total, node.right)

        x = func(sum_total, root)

        return x