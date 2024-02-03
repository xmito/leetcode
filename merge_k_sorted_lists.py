from typing import Optional, List
from queue import PriorityQueue


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

    def __str__(self):
        return f"ListNode({self.val}, {self.next})"


# Merge K Sorted Lists (Hard)
# You are given an array of k linked-lists lists, each linked-list is sorted
# in ascending order. Merge all the linked-lists into one sorted linked-list
# and return it.

# Constraints:
# k == lists.length
# 0 <= k <= 10ˆ4
# 0 <= lists[i].length <= 500
# -10ˆ4 <= lists[i][j] <= 10ˆ4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 10ˆ4.


# TIME COMPLEXITY: O(n * logk)
# n - iterations to merge each list node
# logk - sort k values in each iteration
# SPACE COMPLEXITY: O(n) - timsort
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    begin, end = None, None
    lists = list(filter(lambda x: x is not None, lists))

    while lists:
        lists = sorted(lists, key=lambda x: x.val)
        if begin is None:
            begin = lists[0]
            end = begin
        else:
            end.next = lists[0]
            end = end.next

        lists[0] = lists[0].next
        if lists[0] is None:
            del lists[0]

    return begin


# TIME COMPLEXITY: O(n * logk)
# SPACE COMPLEXITY: O(n) - priority queue
def mergeKListsPrio(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    head = point = ListNode(0)
    q = PriorityQueue()
    for l in lists:
        if l:
            q.put((l.val, l))
    while not q.empty():
        val, node = q.get()
        point.next = ListNode(val)
        point = point.next
        node = node.next
        if node:
            q.put((node.val, node))

    return head.next


def merge(lst_a, lst_b):
    head = point = ListNode(0)
    while lst_a and lst_b:
        if lst_a.val < lst_b.val:
            point.next = lst_a
            lst_a = lst_a.next
        else:
            point.next = lst_b
            lst_b = lst_b.next
        
        point = point.next

    if lst_a:
        point.next = lst_a
    elif lst_b:
        point.next = lst_b

    return head.next

# TIME COMPLEXITY: O(n * logk)
# SPACE COMPLEXITY: O(logk)
def mergeKListsDQ(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return
    elif len(lists) < 2:
        return lists[0]

    pivot = len(lists) // 2
    lst_a = mergeKListsDQ(lists[:pivot])
    lst_b = mergeKListsDQ(lists[pivot:])
    return merge(lst_a, lst_b)


if __name__ == "__main__":
    for fun in [mergeKLists, mergeKListsPrio, mergeKListsDQ]:
        ret = fun([
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(2, ListNode(6)),
        ])
        for val in [1,1,2,3,4,4,5,6]:
            assert ret.val == val
            ret = ret.next
        assert ret is None

        ret = fun([])
        assert ret is None

        ret = fun([ListNode(None)])
        assert ret
        assert ret.val is None
        assert ret.next is None
