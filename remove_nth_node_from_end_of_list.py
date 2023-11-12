from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Remove Nth Node From End of List (Medium)
# Given the head of a linked list, remove the nth node from the end
# of the list and return its head.
# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
def list_len(head):
    if head is None:
        return 0

    count = 1
    while head.next:
        count += 1
        head = head.next
    return count

# Time complexity: O(n)
# Space complexity: O(1)
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # Index for node to remove
    length = list_len(head)
    index = length - n
    
    # In case index to remove is not valid
    if index < 0:
        raise ValueError

    prev, curr = head, head
    for i in range(index):
        prev = curr
        curr = curr.next

    prev.next = curr.next
    if prev is curr:
        return curr.next
    
    return head


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = removeNthFromEnd(head, n=2)
    for val in [1,2,3,5]:
        assert res and res.val == val
        res = res.next
    assert res is None

    head = ListNode(1)
    res = removeNthFromEnd(head, n=1)
    assert res is None

    head = ListNode(1, ListNode(2))
    res = removeNthFromEnd(head, n=1)
    assert res and res.val == 1 and res.next is None
