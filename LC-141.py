# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow_ptr = head
        if not head:
            return False
        if head.next == None:
            return False

        fast_ptr = head.next

        l = 0

        if l == 1:
            return False

        while (fast_ptr != slow_ptr and fast_ptr.next and fast_ptr.next.next):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        if fast_ptr == slow_ptr:
            return True
        else:
            return False


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow=fast=head
        while(slow!=None and fast!=None and fast.next):
            if slow==fast.next:
                return True
            else:
                slow=slow.next
                fast=fast.next.next
        return False