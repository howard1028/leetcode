from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        d = deque([root])
        res = []
        
        # 全部node跑過一次
        # while d is not None: # 變成空也不代表是None
        while d:
            current_level = []
            level_node_num = len(d)

            # 每次把該層node放到current_level
            for i in range(level_node_num):
                node = d.popleft()
                current_level.append(node.val)

                # 把相鄰的node放到deque內
                if node.left is not None:
                    d.append(node.left)
                if node.right is not None:
                    d.append(node.right)
            res.append(current_level)
        return res