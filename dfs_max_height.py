# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node):
            return 0 if node is None else max(dfs(node.left), dfs(node.right)) + 1

        return dfs(root)
