# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []
        def postorder(node , order):
            # L
            if node.left is not None:
                postorder(node.left , order)
            # R
            if node.right is not None:
                postorder(node.right , order)
            # D
            order.append(node.val)
        if root is not None:
            postorder(root,order)
        return order