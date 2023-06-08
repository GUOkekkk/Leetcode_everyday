# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return
        # it is necessary here to do the iteration
        cur = head

        # copy the next
        while cur:
            dum = Node(cur.val)
            dum.next = cur.next
            cur.next = dum
            cur = dum.next

        # copy the random
        # start from the head again
        cur = head
        while cur:
            # choose the old node(new node does not has the random), not exactlly true, some old node also has null random
            # but we could skip it
            if cur.random:
                # the reason why using cur.random.next here is to connet the new node to the new node
                cur.next.random = cur.random.next
            cur = cur.next.next

        # split
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next

        # keep the origin linked
        pre.next = None

        # return the copy new linked head node
        return res
