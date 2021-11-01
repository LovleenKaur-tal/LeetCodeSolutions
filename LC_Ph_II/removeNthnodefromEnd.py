# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        count = 0
        tmp = head
        tmp2 = head
        while (tmp):
            tmp = tmp.next
            count = count + 1

        left = count - n

        c = 0
        if c == 0 and c == left and head:
            return head.next

        while (c != left - 1 and head):
            head = head.next

            c = c + 1
        curr = head
        nxt = None

        if head:
            nxt = head.next


        if nxt:
            curr.next = nxt.next
            nxt.next = None
        else:
            if curr:
                curr.next = nxt
            else:
                curr = None
        return tmp2
