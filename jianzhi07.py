from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# cause the preorder is root, left, right, inorder is left, root, right
# so the first element of preorder is root, and find the root in inorder, the left is left tree, the right is right tree
# and then based on the number in inorder, we can find the number of left tree and right tree in preorder
# partion
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        # find the index of root in inorder
        index = inorder.index(preorder[0])
        # recursion; build the left and right tree
        root.left = self.buildTree(preorder[1 : index + 1], inorder[:index])
        root.right = self.buildTree(preorder[index + 1 :], inorder[index + 1 :])
        return root


# A faster method: A bit complexed...
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recur(root, left, right):
            if left > right:
                return  # left is over the right, return

            node = TreeNode(preorder[root])  # build the root node
            i = dic[preorder[root]]  # find the index of root in inorder

            # how to find the root in the subtree is the key
            # cause it is the preorder, so for sure the next left subtree root is the root + 1
            node.left = recur(root + 1, left, i - 1)  # recursion the left tree

            # but this part is a bit hard to understand
            # the next right subtree root is the root + the length of left tree + 1
            # and the left tree length is i - left
            node.right = recur(i - left + root + 1, i + 1, right)  # recursion the right tree
            return node  # return the root node

        # use the dict as the hash table to save the time
        dic, preorder = {}, preorder

        # save the inorder index in the dict
        for i in range(len(inorder)):
            dic[inorder[i]] = i

        # give the root, left, right to the recur function
        return recur(0, 0, len(inorder) - 1)
