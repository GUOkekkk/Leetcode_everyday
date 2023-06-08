# Definition for singly-linked list.

from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        # use stack to reverse the list
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(2)
    print(s.reversePrint(head))
