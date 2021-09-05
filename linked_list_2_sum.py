# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        final_node = ListNode()
        tmp = final_node
        carry = 0

        while (l1 != None or l2 != None or carry):

            a = l1.val if l1 and l1.val else 0
            b = l2.val if l2 and l2.val else 0
            c = a + b + carry
            carry = c // 10
            va = c % 10

            final_node.val = int(va)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if l1 or l2 or carry:
                final_node.next = ListNode()
                final_node = final_node.next
        return tmp







