from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Swap Nodes in Pairs (Medium)
# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)
# Constraints:
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100
def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return
    
    prev = ListNode(None)
    final = head.next or head
    while head:
        next = head.next
        if next is None:
            break
        
        head.next = next.next
        next.next = head
        prev.next = next

        prev = head
        head = head.next

    return final


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    res = swapPairs(head)
    for val in [2, 1, 4, 3]:
        assert res.val == val
        res = res.next
    assert res is None

    res = swapPairs(None)
    assert res == None

    head = ListNode(1)
    res = swapPairs(head)
    assert res.val == 1 and res.next is None
