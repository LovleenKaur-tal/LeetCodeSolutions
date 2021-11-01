# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """






        # Remove from the middle
        ptr = tmp = head
        ll = 0
        while(head):
            head=head.next
            ll = ll+1

        iter_till = ll-n

        # remove from beginning
        if n == 1:
            if ll == 1:
                return head
        # remove from beginning
        if n==ll:
            return ptr.next


        it = 0
        while(it < iter_till-1):
            tmp = tmp.next
            it = it+1

        node_to_remove = tmp.next
        if node_to_remove.next:
            tmp.next = node_to_remove.next
        else:
            tmp.next = None
        return ptr






        