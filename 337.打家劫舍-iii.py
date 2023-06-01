#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        def _rob(root):
            if not root: return 0, 0

            ls, ln = _rob(root.left) # ls: 左子树偷，ln: 左子树不偷
            rs, rn = _rob(root.right) # rs: 右子树偷，rn: 右子树不偷

            # root偷，左右子树都不能偷
            # root不偷，左右子树偷或不偷都可以, 取最大值, not has to steal from left or right
            return root.val + ln + rn, max(ls, ln) + max(rs, rn)

        return max(_rob(root))
# @lc code=end

if __name__ == '__main__':
    test = Solution()
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)
    print(test.rob(root))
