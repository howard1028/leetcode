# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def DFS(node):
            if node is None:
                return 0

            # L
            left_depth = DFS(node.left)
            # R
            right_depth = DFS(node.right)
            # D
            diameter = left_depth + right_depth
            self.max_diameter = max(self.max_diameter, diameter)

            return 1 + max(left_depth, right_depth)

        self.max_diameter = 0
        DFS(root)
        return self.max_diameter
