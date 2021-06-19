# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        leftList = ListNode()
        rightList = ListNode()
        ltail = leftList
        rtail = rightList

        while (head):
            if head.val < x:
                ltail.next = head;
                ltail = ltail.next
            else:
                rtail.next = head;
                rtail = rtail.next
            head = head.next

        ltail.next = rightList.next
        rtail.next = None

        return leftList.next


