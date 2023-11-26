import sys
from typing import Optional

# Validate Binary Search Tree (Medium)
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# * The left subtree of a node contains only nodes with keys less than the node's key.
# * The right subtree of a node contains only nodes with keys greater than the node's key.
# * Both the left and right subtrees must also be binary search trees.
# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -2ˆ31 <= Node.val <= 2ˆ31 - 1

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity: O(n)
# Space complexity: O(n) - call stack
def isValidBST(root: Optional[TreeNode]) -> bool:
    def recurse(root: Optional[TreeNode], lo, hi) -> bool:
        if root is None:
            return True

        if root.val <= lo or root.val >= hi:
            return False

        return recurse(root.left, lo, root.val) and recurse(root.right, root.val, hi)
    
    return recurse(root, -sys.maxsize - 1, sys.maxsize)


if __name__ == "__main__":
    root = TreeNode(5, left=TreeNode(4), right=TreeNode(6, left=TreeNode(3), right=TreeNode(7)))
    res = isValidBST(root)
    assert res == False

    root = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    res = isValidBST(root)
    assert res == True

    root = TreeNode(5, left=TreeNode(1), right=TreeNode(4, left=TreeNode(3), right=TreeNode(6)))
    res = isValidBST(root)
    assert res == False