# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


# BFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

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
