from typing import List


# # check if it is a postorder traversal of a binary search tree by creating the tree
# class Solution:
#     def verifyPostorder(self, postorder: List[int]) -> bool:
#         def build(postorder: List[int], ma: int, mi: int):
#             if not postorder:
#                 return
#             # the last of the list is the root node
#             val = postorder[-1]

#             # break if the root node is not in the range
#             if not mi < val < ma:
#                 return

#             # pop the root node
#             postorder.pop()

#             # recursively build the right subtree, the mi is the val
#             build(postorder, ma, val)

#             # recursively build the left subtree, the ma is the val
#             build(postorder, val, mi)

#         build(postorder, sys.maxsize, -sys.maxsize)
#         # if the postorder is valid, the list will be empty
#         return not postorder

# this question should be solve from the end of the list


# class Solution:
#     def verifyPostorder(self, postorder: [int]) -> bool:
#         def recur(i, j):
#             # i and j is the left and right index of the list, if left over the right, return True
#             # the bread condition of the recursion, especially it is a tree problem,
#             # left over the right means it the leaf node
#             if i >= j:
#                 return True
#             p = i
#             while postorder[p] < postorder[j]:
#                 p += 1
#             # find the m which is the first element that is larger than the root node
#             m = p
#             # m is the start of the right subtree, so all the elements in the right subtree should be larger than the root node
#             while postorder[p] > postorder[j]:
#                 p += 1
#             # partion the list into two parts, the left part is the left subtree, the right part is the right subtree
#             return p == j and recur(i, m - 1) and recur(m, j - 1)

#         return recur(0, len(postorder) - 1)


# it is define a rule to traverse the list to check if it is a postorder traversal of a binary search tree
# for the BST, the left subtree is smaller than the root node, the right subtree is larger than the root node, all nodes!
# ? NOT SURE need to check
class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        stack, root = [], float("+inf")
        # traverse the list from the end
        for i in range(len(postorder) - 1, -1, -1):
            # if the current node is larger than the root node, return False
            if postorder[i] > root:
                return False
            # if the current node is smaller than the root node, it is the left subtree, and we should find the root node of the subtree
            # when meet a decreasing node, find its root node, and the rest node is the left subtree so should be smaller than the root node
            # use this stack to store the monotonic increasing nodes, and the root should be the smaller one
            while stack and postorder[i] < stack[-1]:
                # find the new root node of the subtree
                root = stack.pop()
            # stack the increasing nodes
            stack.append(postorder[i])
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.verifyPostorder([1, 3, 2, 7, 4, 6, 5]))
