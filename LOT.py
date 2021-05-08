# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = deque()
        q.append(root)

        result = []
        while (q):
            l = []
            for i in range(0, len(q)):
                node = q.popleft()

                if node:
                    l.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if l:
                result.append(l)

        return result

