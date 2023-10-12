# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow =head #兩個pointer指到head
        while fast and fast.next: #當fast是null或fast的下一個是空，停
            slow=slow.next
            fast=fast.next.next #fast一次走兩個，slow一次走一個
        return slow
        