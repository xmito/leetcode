from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Reverse Nodes in K-Group (Hard)
# Given the head of a linked list, reverse the nodes of the list k at a time,
# and return the modified list. k is a positive integer and is less than or
# equal to the length of the linked list. If the number of nodes is not a
# multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves
# may be changed.

# Constraints:
# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000


# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)
def reverse(start, end):
    prev = ListNode(None, None)
    while start != end:
        next = start.next
        start.next = prev
        prev = start
        start = next
    start.next = prev


# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)
def jump(node, steps):
    for i in range(steps):
        if node is None:
            break
        node = node.next
    return node


# TIME COMPLEXITY: O(n) - constant amount of work for each node
# SPACE COMPLEXITY: O(n/k) - recursion stack depth
def reverseKGroupRecursive(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    start, end = head, head
    end = jump(end, steps=k - 1)
    if end:
        post = end.next
        reverse(start, end)
        start.next = reverseKGroupRecursive(post, k)
        return end

    return start
 

# TIME COMPLEXITY: O(n) - two traversals, one for counting and another for reversal
# SPACE COMPLEXITY: O(1)
def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    initial = None
    pre = ListNode(None, None)
    start, end = head, head

    end = jump(end, steps=k - 1)

    while end:
        post = end.next
        reverse(start, end)
        pre.next = end
        start.next = post

        if initial is None:
            initial = end

        pre = start
        start, end = post, post
        end = jump(end, steps=k - 1)

    return initial            


if __name__ == "__main__":
    for fun in [reverseKGroupRecursive, reverseKGroup]:
        lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        res = fun(lst, 2)
        for val in [2,1,4,3,5]:
            assert res.val == val
            res = res.next
        assert res is None

        lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        res = fun(lst, 3)
        for val in [3,2,1,4,5]:
            assert res.val == val
            res = res.next
        assert res is None
