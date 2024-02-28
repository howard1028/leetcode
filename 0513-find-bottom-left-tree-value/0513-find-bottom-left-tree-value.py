from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        d = deque([root])
        leftmost = root.val

        while len(d) != 0:
            level_size = len(d)
            for i in range(level_size):
                p = d.popleft()
                if i == 0:
                    leftmost = p.val 
                if p.left is not None:
                    d.append(p.left)
                if p.right is not None:
                    d.append(p.right)
        return leftmost