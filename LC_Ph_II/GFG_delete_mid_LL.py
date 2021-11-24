'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


def deleteMid(head):
    '''
    head:  head of given linkedList
    return: head of resultant llist
    '''

    fast_ptr = head
    slow_ptr = head
    prev = head

    while (fast_ptr and fast_ptr.next):
        prev = slow_ptr
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    prev.next = slow_ptr.next

    return head
