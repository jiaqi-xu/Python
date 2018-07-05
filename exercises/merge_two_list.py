# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# way_1
def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    list_header = ListNode(0)
    p = list_header
    while l1 is not None or l2 is not None:
        if l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        elif l1 is not None and l2 is None:
            p.next = l1
            break
        else:
            p.next = l2
            break

    return list_header.next

# way2
def mergeTwoLists_2(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    if l1 is None:
        return l2

    if l2 is None:
        return l1

    p = ListNode(0)
    if l1.val <= l2.val:
        p = l1
        p.next = mergeTwoLists(l1.next, l2)
    else:
        p = l2
        p.next = mergeTwoLists(l1, l2.next)

    return p