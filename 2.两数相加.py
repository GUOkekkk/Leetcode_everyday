#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p = dummy
        carry = 0  # 保存进位
        p1 = l1
        p2 = l2
        while p1 or p2:
            first, second = 0, 0
            if p1:
                first = p1.val
                p1 = p1.next
            if p2:
                second = p2.val
                p2 = p2.next
            result = carry + first + second
            p.next = ListNode(result % 10)
            carry = result // 10
            p = p.next

        # 如果所有的节点都计算完后，还有进位，也需要保存下来
        if carry:
            p.next = ListNode(carry)

        return dummy.next


# @lc code=end
