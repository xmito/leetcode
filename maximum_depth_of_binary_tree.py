from typing import Optional

# Maximum Depth of Binary Tree (Easy)
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity: O(n)
# Space complexity: O(n)
def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    return max(maxDepth(root.left), maxDepth(root.right)) + 1


if __name__ == "__main__":
    root = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    res = maxDepth(root)
    print(res)
    assert res == 3

    root = TreeNode(1, right=TreeNode(2))
    res = maxDepth(root)
    print(res)
    assert res == 2
