# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenB = lenA = 0
        tmpA = headA
        tmpB = headB
        while (tmpA != None):
            tmpA = tmpA.next
            lenA = lenA + 1
        while (tmpB != None):
            tmpB = tmpB.next
            lenB = lenB + 1
        jump = abs(lenA - lenB)
        if lenA > lenB:

            while (jump):
                headA = headA.next
                jump = jump - 1
        else:
            while (jump):
                headB = headB.next
                jump = jump - 1
        while (headA != headB):
            headA = headA.next
            headB = headB.next
            if headA == None or headB == None:
                return None
        return headB






