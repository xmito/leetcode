from typing import Optional
from collections import deque

# Minimum Depth of Binary Tree (Easy)
# Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along
# the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.
# Constraints:
# The number of nodes in the tree is in the range [0, 10ˆ5].
# -1000 <= Node.val <= 1000

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity: O(n)
# Space complexity: O(n)
def minDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    if root.right is None:
        return minDepth(root.left) + 1
    elif root.left is None:
        return minDepth(root.right) + 1

    return min(minDepth(root.left), minDepth(root.right)) + 1


# Time complexity: O(n)
# Space complexity: O(n)
def minDepthIterative(root: Optional[TreeNode]) -> int:
    queue = deque([(root, 1)])
    while queue:
        root, depth = queue.popleft()

        if root is None:
            continue

        if root.left is None and root.right is None:
            return depth

        queue.append((root.left, depth + 1))
        queue.append((root.right, depth + 1))
    
    return 0


if __name__ == "__main__":
    root = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    res = minDepth(root)
    print(res)
    assert res == 2

    root = TreeNode(1, right=TreeNode(2, right=TreeNode(3, right=TreeNode(4, right=TreeNode(5, right=TreeNode(6))))))
    res = minDepth(root)
    print(res)
    assert res == 6
