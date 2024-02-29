from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        def even_odd(value , depth):
            # 滿足奇數層為偶數，偶數層為奇數
            if depth % 2 == 0:
                if value % 2 == 0:
                    return False
            else:
                if value % 2 == 1:
                    return False
            return True

        d = deque([root])
        depth = 0

        while len(d) > 0:
            level_size = len(d)
            for i in range(level_size):
                node = d.popleft()
                # check奇偶
                if not even_odd(node.val , depth):
                    return False
                # check奇數層遞減，偶數層遞增
                if i == 0:
                    temp = node.val
                if depth % 2 == 1:
                    if temp <= node.val and i != 0:
                        # print("1")
                        return False
                else:
                    if temp >= node.val and i != 0:
                        # print("2",temp , node.val)
                        return False
                temp = node.val

                # 左右放進deque
                if node.left is not None:
                    d.append(node.left)
                if node.right is not None:
                    d.append(node.right)
            # 到下一層
            depth += 1
        return True