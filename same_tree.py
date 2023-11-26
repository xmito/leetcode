from typing import Optional
from collections import deque

# Same Tree (Easy)
# Given the roots of two binary trees p and q, write a function to check if they are the same
# or not. Two binary trees are considered the same if they are structurally identical, and the
# nodes have the same value.
# Constraints:
# The number of nodes in both trees is in the range [0, 100].
# -10ˆ4 <= Node.val <= 10ˆ4


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity: O(n)
# Space complexity: O(n) - unbalanced tree has linear stack
def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False

    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# Time complexity: O(n)
# Space complexity: O(n) - BFS has to store at least one entire tree level. Last level has n / 2 nodes
def isSameTreeIterative(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    queue = deque([(p, q)])
    while queue:
        a, b = queue.pop()
        if a is None and b is None:
            continue
        elif a is None or b is None:
            return False
        
        if a.val != b.val:
            return False
        
        queue.append((a.left, b.left))
        queue.append((a.right, b.right))
    
    return True
    

if __name__ == "__main__":
    root = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    res = isSameTree(root, root)
    assert res == True

    root1 = TreeNode(1, left=TreeNode(2))
    root2 = TreeNode(1, right=TreeNode(2))
    res = isSameTree(root1, root2)
    assert res == False

    root1 = TreeNode(1, left=TreeNode(2), right=TreeNode(1))
    root2 = TreeNode(1, left=TreeNode(1), right=TreeNode(2))
    res = isSameTree(root1, root2)
    assert res == False
