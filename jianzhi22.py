# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# the difficulty is for the linked list, we can not get the length of the linked list
# if we travel the linked list, we can get the length of the linked list but time complexity is O(n)
# we define two pointers, one is fast pointer, another is slow pointer, the distance between them is k
# when the fast pointer reach the end, the slow pointer is the kth node from the end
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        fast = head
        slow = head
        for _ in range(k):
            # consider the case that k is larger than the length of the linked list
            if fast is None:
                return None
            fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
        return slow
