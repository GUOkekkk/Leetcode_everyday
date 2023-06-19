#  Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# it is a binary search tree, so the left node is smaller than the root node, and the right node is bigger than the root node
# when it is BST, we consider use the inorder traversal, cause the inorder traversal is ordered
# but actually, we don't need to traversal all the tree, we just need to traversal the kth node and inverse the inorder traversal
# class Solution:
#     def kthLargest(self, root: TreeNode, k: int) -> int:
#         self.res = []

#         def inorder(root):
#             if not root:
#                 return
#             inorder(root.left)
#             self.res.append(root.val)
#             inorder(root.right)

#         inorder(root)
#         return self.res[-k]


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            if self.k == 0:
                return
            # find a root node should be start from the biggest node
            self.k -= 1
            # find the kth node, record the value
            if self.k == 0:
                self.res = root.val
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    k = 1
    s = Solution()
    print(s.kthLargest(root, k))
