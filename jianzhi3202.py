# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


# BFS but count the level
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        # use the turple to store the level
        queue = [(root, 0)]
        res = []

        while queue:
            node, level = queue.pop(0)

            # check the level
            if len(res) == level:
                # create an empty list to store each level
                res.append([])

            # add the node to different level
            res[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return res


if __name__ == "__main__":
    test = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(test.levelOrder(root))
