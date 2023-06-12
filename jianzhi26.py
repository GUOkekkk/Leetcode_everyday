# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# this one is hard to solve, need to draw the tree to understand, have a clear analysis process
# especially the recur function, if not B means the check of B is done
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        # bool(A and B) to check if A and B are not None
        # recur(A, B) to check if A and B are the same
        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))
