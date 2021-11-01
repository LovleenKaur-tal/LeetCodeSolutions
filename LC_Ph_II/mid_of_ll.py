# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = 0
        tmp = head
        while (tmp):
            l = l + 1
            tmp = tmp.next
        mid = abs(l // 2)
        count = 0

        while (count != mid):
            head = head.next
            count = count + 1
        return head




