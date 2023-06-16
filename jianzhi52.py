# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not (headA and headB):
            return None
        # we can use the two pointer to travel the linked list, if they are the same, we return the node
        # cause a + b - c = b + a - c, so we can use the two pointer to travel the linked list, if pointer is None,
        # start from the other head
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA


if __name__ == "__main__":
    test = Solution()
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = ListNode(8)
    headA.next.next.next = ListNode(4)
    headA.next.next.next.next = ListNode(5)
    headB = ListNode(5)
    headB.next = ListNode(0)
    headB.next.next = ListNode(1)
    headB.next.next.next = headA.next.next
    print(test.getIntersectionNode(headA, headB).val)
