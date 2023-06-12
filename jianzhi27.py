# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# need to copy a new Treenode
# this seems a bit wrong, we need to modify the original tree
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        new_root = TreeNode(root.val)
        # just swap the left and right and use the recursion
        new_root.left = self.mirrorTree(root.right)
        new_root.right = self.mirrorTree(root.left)
        return new_root


# not return a new TreeNode
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        # but if it is not in python, we need to use a temp variable to store the value
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root
