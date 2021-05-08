# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        q = deque()

        q.append(root)
        flag = True
        result = []

        while (q):
            l = []
            for i in range(0, len(q)):
                node = q.popleft()
                if node:
                    l.append(node.val)

                    q.append(node.left)
                    q.append(node.right)
            if l and flag:
                result.append(l)
                flag = False
            elif l and not flag:
                result.append(l[::-1])
                flag = True

        return result





