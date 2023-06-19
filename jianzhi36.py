# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: "Node") -> "Node":
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)  # 递归左子树
            if self.pre:  # 修改节点引用
                # pre -> <- cur
                self.pre.right, cur.left = cur, self.pre
            else:  # 记录头节点
                self.head = cur
            # iterative
            self.pre = cur  # 保存 cur
            dfs(cur.right)  # 递归右子树

        # special case
        if not root:
            return

        self.pre = None
        dfs(root)
        # connect head and tail
        self.head.left, self.pre.right = self.pre, self.head
        return self.head
