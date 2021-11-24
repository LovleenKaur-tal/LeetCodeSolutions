'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''


class Solution:
    def addOne(self, head):
        # Returns new head of linked List.
        dummy = Node(data=0)
        dummy.next = head
        last_non_9_digit = dummy
        tmp = head

        while (tmp):
            if tmp.data != 9:
                last_non_9_digit = tmp
            tmp = tmp.next

        last_non_9_digit.data = last_non_9_digit.data + 1
        last_non_9_digit = last_non_9_digit.next

        while (last_non_9_digit):
            last_non_9_digit.data = 0
            last_non_9_digit = last_non_9_digit.next
        if dummy.data == 0:
            return dummy.next
        else:

            return dummy
