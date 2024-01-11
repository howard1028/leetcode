# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []

        def inorder(node,order):
            # L
            if node.left is not None: 
                inorder(node.left , order)
            # D
            order.append(node.val)
            # R
            if node.right is not None:
                inorder(node.right , order)

        if root is not None:
            inorder(root , order)

        return order