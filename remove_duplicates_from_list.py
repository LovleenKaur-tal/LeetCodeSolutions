# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        t = head
        while (head != None):

            if head.next and head.val == head.next.val:

                dump = head.next
                head.next = head.next.next

                dump.next = None

            else:
                head = head.next

        return t



