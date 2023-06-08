# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        # add the following two lines to reverse the list, and return the all list
        head.next.next = head
        head.next = None
        return p


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(2)
    print(s.reverseList(head))
