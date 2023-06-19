# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List


# should be a DFS problem
# we need two lists, one is the path, one is the result
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        # we need to maintain a path list
        def dfs(node, target, path):
            if not node:
                return
            if not node.left and not node.right and target == node.val:
                path.append(node.val)
                res.append(path)
                return
            dfs(node.left, target - node.val, path + [node.val])
            dfs(node.right, target - node.val, path + [node.val])

        res = []
        dfs(root, target, [])
        return res


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []

        def recur(root, tar):
            if not root:
                return
            path.append(root.val)
            tar -= root.val

            # it is a leaf node and the value is equal to the target
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))

            # first go left, then go right, new target
            recur(root.left, tar)
            recur(root.right, tar)

            # this node is not what we need, pop out
            path.pop()

        recur(root, sum)
        return res
