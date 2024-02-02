from math import floor
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Add Two Numbers (Medium)
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list. You may assume the two numbers do not contain any leading zero, except
# the number 0 itself.

# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# TIME COMPLEXITY: O(max(logn, logm)) - sum digits in two numbers
# SPACE COMPLEXITY: O(1)
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode(0)
    current = head
    carry = 0

    while l1 or l2 or carry:
        l1val = l1.val if l1 else 0
        l2val = l2.val if l2 else 0
        
        colsum = (l1val + l2val + carry)
        carry = colsum // 10

        node = ListNode(colsum % 10)
        current.next = node
        current = node

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return head.next

        
if __name__ == "__main__":
    ret = addTwoNumbers(
        ListNode(2, ListNode(4, ListNode(3))),
        ListNode(5, ListNode(6, ListNode(4))),
    )
    for num in [7, 0, 8]:
        assert ret.val == num
        ret = ret.next

    ret = addTwoNumbers(ListNode(0), ListNode(0))
    assert ret and ret.val == 0 and ret.next is None

    ret = addTwoNumbers(
        ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
        ListNode(9, ListNode(9, ListNode(9, ListNode(9)))),
    )
    for num in [8,9,9,9,0,0,0,1]:
        assert ret.val == num
        ret = ret.next