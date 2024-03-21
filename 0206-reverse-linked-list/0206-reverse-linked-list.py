# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # recursive 遞迴

#         # 結束條件
#         if not head or head.next is None:
#             return head
#         # head 跑到最後
#         new_head = self.reverseList(head.next)
#         # reverse
#         head.next.next = head
#         head.next = None

#         return new_head

        # iteration 迭代

        prev = None
        curr = head

        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode 
        
        return prev