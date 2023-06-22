# the DFS is based on the recursion or stack
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # the node is none
        if not root:
            return 0
        # recursion the root depth = max(left, right) + 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# THe BFS is based on the queue
# after traversing all the nodes in the same level, the depth + 1
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # the node is none
        if not root:
            return 0
        # initialize the queue and the depth
        queue, res = [root], 0

        # while the queue is not empty
        while queue:
            tmp = []
            # traverse all the nodes in the same level
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
            res += 1
        return res
