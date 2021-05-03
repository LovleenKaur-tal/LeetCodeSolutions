# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        dummy = tmp = ListNode(0, head)
        while (tmp != None):
            if tmp and tmp.next and tmp.next.val == val:
                save = tmp.next
                if save:
                    tmp.next = save.next
                else:
                    tmp.next = None
                save = None
            else:
                tmp = tmp.next
        return dummy.next


