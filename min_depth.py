# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        q = deque()
        q.append(root)
        count = 0
        if not root:
            return 0

        while (q):
            count = count + 1
            for i in range(0, len(q)):
                node = q.popleft()

                if node and node.left == None and node.right == None:
                    return count
                elif node:
                    q.append(node.left)
                    q.append(node.right)
        return count




"""
DFS and break when left and right child is None

"""