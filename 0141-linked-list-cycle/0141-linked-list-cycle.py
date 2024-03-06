# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 0 or 1 個node
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        # slow 還沒被 fast 追上
        while slow != fast:
            # fast 走到底了
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True