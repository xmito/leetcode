from typing import Optional, List

# Find Leaves of Binary Tree (Medium)
# Given the root of a binary tree, collect a tree's nodes as if you were doing this:
# * Collect all the leaf nodes.
# * Remove all the leaf nodes.
# * Repeat until the tree is empty.
# Constraints:
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity: O(n) - Each node is traversed exactly once
# Space complexity: O(1) - we don't consider leaves (because it is result)
def findLeaves(root: Optional[TreeNode]) -> List[List[int]]:
    def recurse(node, leaves) -> int:
        if node.left is None and node.right is None:
            if len(leaves) == 0:
                leaves.append([])
            leaves[0].append(node.val)
            return 0

        left, right = 0, 0
        if node.left:
            left = recurse(node.left, leaves)
        if node.right:
            right = recurse(node.right, leaves)

        height = max(left, right) + 1
        if len(leaves) == height:
            leaves.append([])
        leaves[height].append(node.val)

        return height

    leaves = []
    recurse(root, leaves)
    return leaves


if __name__ == "__main__":
    root = TreeNode(
        1,
        left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
        right=TreeNode(3)
    )
    res = findLeaves(root)
    print(res)
    assert res == [[4,5,3],[2],[1]]
