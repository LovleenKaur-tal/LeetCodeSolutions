# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        curr = fast = slow = head

        while (slow != None and fast != None and fast.next):
            fast = fast.next.next
            slow = slow.next

            """
            Why if is below because otherwise the slow and fast will be equal hence it will break in the beginning itself.
            """
            if slow == fast:
                break
        if fast == None or slow == None:
            return None
        if fast.next == None or slow.next == None:
            return None

        while (curr != slow):
            slow = slow.next
            curr = curr.next

        return curr
