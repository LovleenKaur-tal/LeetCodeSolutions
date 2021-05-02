# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if head.next == None:
            return head
        if k == 0:
            return head
        tmp = head
        l = 0
        while (tmp):
            tmp = tmp.next
            l = l + 1
        k = k % l

        main = head
        if k == 0:
            return head
        for i in range(0, l - k - 1):
            head = head.next
        first_node = head.next
        head.next = None
        new_nn = first_node

        while (new_nn and new_nn.next != None):
            new_nn = new_nn.next
        if new_nn:
            new_nn.next = main
        return first_node


