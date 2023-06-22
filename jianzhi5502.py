# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            # the node is none
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            # if it is not balanced, return -1
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            else:
                # if it is balanced, return the depth
                return max(left, right) + 1

        return dfs(root) != -1


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if not root:
                return 0
            # save more time
            left = recur(root.left)
            if left == -1:
                return -1

            right = recur(root.right)
            if right == -1:
                return -1
            # check if it is balanced
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        # check every node and its left and right subtree
        # recursively
        return (
            abs(self.depth(root.left) - self.depth(root.right)) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )

    # get the depth of the node
    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
