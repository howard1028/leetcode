# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []
        def preorder(node, order):
            # D
            order.append(node.val)
            # L
            if node.left is not None:
                preorder(node.left , order)
            # R
            if node.right is not None:
                preorder(node.right , order)
        if root is not None:
            preorder(root,order)
        return order