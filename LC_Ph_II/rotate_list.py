# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        first_node = head
        count = 0
        le = head
        while (le):
            le = le.next
            count = count + 1
        total_length = count
        if not total_length:
            return head
        if k % total_length == 0:
            return first_node
        k = k % total_length

        count = 0
        while (count < total_length - k - 1):
            head = head.next
            count = count + 1
        tmp = part_1 = head.next
        head.next = None

        while (part_1 and part_1.next):
            part_1 = part_1.next

        if part_1:
            part_1.next = first_node
        else:
            return first_node

        return tmp


