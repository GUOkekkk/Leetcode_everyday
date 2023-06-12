# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # use the recursion, define a recursion function -> what is the break condition, what is the contine condition
        def recur(L, R):
            # the left and right are all None
            if not L and not R:
                return True
            # not abide, break, the L and R are not the same
            if not L or not R or L.val != R.val:
                return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        # if no root, return True
        return recur(root.left, root.right) if root else True


if __name__ == "__main__":
    test = Solution()
    # the input is like [1,2,2,null,3,null,3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)
    print(test.isSymmetric(root))
