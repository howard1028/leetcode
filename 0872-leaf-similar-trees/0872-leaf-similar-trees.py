# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def DFS(root , leaf_seq):
            if root is not None:
                if root.left is None and root.right is None:
                    leaf_seq.append(root.val)
                if root.left is not None:
                    DFS(root.left , leaf_seq)
                if root.right is not None:
                    DFS(root.right , leaf_seq)

        leaf1 = []
        leaf2 = []

        DFS(root1 , leaf1)
        DFS(root2 , leaf2)
        print("l1:",leaf1)
        print("l2:",leaf2)

        if leaf1 == leaf2:
            return True
        else:
            return False