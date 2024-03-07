# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        one = head
        two = head
        while True:
            if not two or not two.next:
                break
            one = one.next
            two = two.next.next
            # print(two.val)
        return one