# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# # define a fake head node and the use the cur pointer to travel the linked list
# # we do not has to keep the l1 or l2
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         # we keep the dum node but travel the cur node
#         # if we define as this why, they have the same address, because they are the same object
#         cur = dum = ListNode(0)
#         # when we have l1 or l2, we can keep the while loop
#         while l1 and l2:
#             if l1.val < l2.val:
#                 # add the smaller one to the cur.next move the l1 or l2
#                 cur.next, l1 = l1, l1.next
#             else:
#                 cur.next, l2 = l2, l2.next
#             # move the cur
#             cur = cur.next
#         # add the no none part
#         cur.next = l1 if l1 else l2
#         return dum.next


# solution 2 by recursion
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not (l1 and l2):
            # if one of them is none, return the other one
            return l1 if l1 else l2
        # return the smaller node, but keep the small node in the new node and move to the next node of smaller node
        if l1.val < l2.val:
            # if l1 is smaller, we keep l1 and move the l1.next and l2
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            # if l2 is smaller, we keep l2 and move the l2.next and l1
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == "__main__":
    test = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    # l1.next.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    # l2.next.next.next = ListNode(4)
    print(test.mergeTwoLists(l1, l2))
