# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# how to use the double pointer to solve the problem
# class Solution:
#     def deleteNode(self, head: ListNode, val: int) -> ListNode:
#         if head.val == val:
#             return head.next

#         while head.next is not None:
#             if head.next.val == val:
#                 head.next = head.next.next
#                 break
#             # can not iterate the head, will lose the before information
#             head = head.next

#         return head


" recursive method "
# class Solution:
#     def deleteNode(self, head: ListNode, val: int) -> ListNode:
#         if head is None:
#             return None
#         if head.val == val:
#             return head.next
#         else:
#             head.next = self.deleteNode(head.next, val)
#             return head


# double pointer, it is not right and left pointer, but pre and cur pointer
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        if head.val == val:
            return head.next
        pre = head
        cur = head.next
        while cur is not None:
            if cur.val == val:
                pre.next = cur.next
                break
            pre = cur
            cur = cur.next
        # can not iterate and change the head, will lose the before information
        return head


if __name__ == "__main__":
    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)

    s = Solution()
    res = s.deleteNode(head, 1)
    while res is not None:
        print(res.val)
        res= res.next
        
