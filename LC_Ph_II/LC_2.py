# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        nn = ListNode()
        c = 0
        c1 = 0
        c2 = 0
        carry = 0

        x = tmp1 = l1
        y = tmp2 = l2
        while l1:
            l1 = l1.next
            c1 = c1 + 1
        while l2:
            l2 = l2.next
            c2 = c2 + 1

        while tmp1 or tmp2:

            if tmp1:
                a = tmp1.val
            else:
                a = 0
            if tmp2:
                b = tmp2.val
            else:
                b = 0
            add = (a + b + carry)
            summ = add % 10

            carry = add / 10 if add != 10 else 1
            nn.val = summ
            if c1 >= c2:
                tmp1.val = summ
            else:
                tmp2.val = summ
            if tmp1:
                tmp1 = tmp1.next
            if tmp2:
                tmp2 = tmp2.next

        p = x
        q = y

        print("")

        if carry and c1 >= c2:
            while (x.next):
                x = x.next
            x.next = ListNode(carry)
            return p
        elif not carry and c1 >= c2:
            return p
        elif carry and c1 < c2:
            while (y.next):
                y = y.next
            y.next = ListNode(carry)

            return q
        else:
            return q







