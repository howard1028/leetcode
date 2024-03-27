# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # 找中間的node(slow)
        slow = head
        fast = head    
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 中間之後reverse
        prev = None
        while slow:
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode

        # 比較從最前面(head)到中間和最後面(prev)到中間是否一樣
        while prev: # 用head可能會多一個node
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        return True

        