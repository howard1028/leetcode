# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def DFS(node):
            # DFS postorder
            # L
            if node.left is not None:
                DFS(node.left)
            # R
            if node.right is not None:
                DFS(node.right)
            # D
            SWAP(node) # swap要最後做   

        def SWAP(node):
            temp = node.left
            node.left = node.right
            node.right = temp

        if root is not None:
            DFS(root)
            
        return root
