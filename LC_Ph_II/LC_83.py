# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        curr_ptr = head
        next_ptr = curr_ptr.next

        while (next_ptr):
            if curr_ptr.val == next_ptr.val:
                curr_ptr.next = next_ptr.next
                next_ptr = next_ptr.next
            else:
                curr_ptr = curr_ptr.next
                next_ptr = next_ptr.next

        return head
