# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = defaultdict(int)

        def height(node , level):
            # preorder
            # D
            level += 1
            depth[level] = node.val # 高度：最右邊node
            # L
            if node.left is not None:
                height(node.left , level)
            # R
            if node.right is not None:
                height(node.right , level)

        if root is not None:
            height(root , level=0)
        else:
            return 0
        print(depth)

        return max(depth)