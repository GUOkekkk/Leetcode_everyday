# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# the tree is a BST and the node values are unique
# cause it is a BST, use its property to solve the problem, like binary search
# So the best is the logN like the binary search and the worst is N like the linked list
# everytime we update the root untill the p and q are in the different side of the root
class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        while root:
            if root.val < p.val and root.val < q.val:  # p and q are in the right subtree
                root = root.right  # go to check the right subtree
            elif root.val > p.val and root.val > q.val:  # p,q are in the left subtree
                root = root.left  # go to check the left subtree
            else:
                break  # they are in the different side of the root
        return root


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        # use this to reduce the compare condition to save time
        if p.val > q.val:
            p, q = q, p  # make sure p.val < q.val, give a order to reduce the time
        while root:
            if root.val < p.val:  #  p and q are in the right subtree
                root = root.right  # go to check the right subtree
            elif root.val > q.val:  # p,q are in the left subtree
                root = root.left  # go to check the left subtree
            else:
                break
        return root


# recursion, do not need the while to save time
class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        if root.val < p.val and root.val < q.val:  # check right subtree
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:  # check left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        return root  # root.val is between p.val and q.val
