from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Merge Two Sorted Lists (Easy)
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by
# splicing together the nodes of the first two lists. Return the head of
# the merged linked list. Both list1 and list2 are sorted in non-decreasing order.
# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode(None)
    merged = head
    while list1 and list2:
        if list1.val < list2.val:
            merged.next = list1
            list1 = list1.next
        else:
            merged.next = list2
            list2 = list2.next
        merged = merged.next
    
    if list1:
        merged.next = list1
    elif list2:
        merged.next = list2

    return head.next


if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    head = mergeTwoLists(list1, list2)
    for val in [1,1,2,3,4,4]:
        assert head.val == val
        head = head.next
    assert head is None

    head = mergeTwoLists(None, None)
    assert head is None

    list1 = None
    list2 = ListNode(0)
    head = mergeTwoLists(list1, list2)
    assert head.val == 0
    assert head.next is None
