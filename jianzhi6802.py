# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# the difference between this and 6801 is that this one is not a binary search tree
# pre-order traversal: root, left, right
# in-order traversal: left, root, right
# post-order traversal: left, right, root
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # special case
        if not root or root == p or root == q:
            return root
        # recursion
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # if one side is None, then the other side is the LCA
        if not left:
            return right
        if not right:
            return left
        # if left and right both exist, then root is the LCA
        return root


#  for k nodes, change the p, q to a list of nodes
class Solution:
    def __init__(self) -> None:
        self.k = 2
        self.res = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.dfs(root, p, q)
        return self.res

    def dfs(self, node, p, q):
        # find the soulution or no node or k == 0
        if self.res or not node or self.k == 0:
            return

        # still have kOld nodes to find
        kOld = self.k

        # find the kth node
        if node.val == p.val or node.val == q.val:
            self.k -= 1

        # dfs
        self.dfs(node.left, p, q)
        self.dfs(node.right, p, q)

        # find the LCA
        # this part it means, before traverse the left and right subtree
        # we did not find k, but after traverse  it, we find all k and not find result before
        # threfore we choose this node as result
        if kOld == 2 and self.k == 0 and not self.res:
            self.res = node
