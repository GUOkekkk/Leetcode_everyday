# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


# BFS(queue) and store the level and change the direction
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = [(root, 0, 0)]  # (node, level, direction)
        res = []
        while queue:
            node, level, direction = queue.pop(0)
            if len(res) == level:
                res.append([])
            if direction == 0:
                res[level].append(node.val)
            else:
                res[level].insert(0, node.val)
            if node.left:
                # use (1 - direction) or (1^direction) to change the direction
                # change bewteen 0 and 1
                # it is much faster to run it here than to run it in the if statement
                queue.append((node.left, level + 1, 1 ^ direction))
            if node.right:
                queue.append((node.right, level + 1, 1 ^ direction))
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
