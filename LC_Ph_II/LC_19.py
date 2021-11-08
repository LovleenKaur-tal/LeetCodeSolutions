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

        len_ptr = head
        l = 0


        while(len_ptr):
            len_ptr=len_ptr.next
            l =l+1
        iter_till = l-n

        # Remove from begiining

        if iter_till == 0:
            head= head.next
            return head

        # remove from middle

        tmp = head
        i =0
        while(i<iter_till-1):
            tmp =tmp.next
            i=i+1

        if tmp.next and tmp.next.next:
            tmp.next = tmp.next.next
        else:
            tmp.next = None

        return head










        