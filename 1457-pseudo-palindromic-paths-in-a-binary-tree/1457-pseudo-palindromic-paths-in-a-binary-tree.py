# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        num = defaultdict(int)  # 紀錄每個數字出現次數

        def judge(num):
            # print(num)
            odd = 0
            for key, value in num.items():
                if value % 2 == 1:
                    odd += 1
            # print(odd)
            if odd == 0 or odd == 1:
                # print("good!")
                return 1
            else:
                return 0

        def keep_going(node, num):
            ppp = 0
            num[node.val] = num.get(node.val, 0) + 1
            # print(num)
            if node.left is not None:
                ppp += keep_going(node.left, num.copy())
            if node.right is not None:
                ppp += keep_going(node.right, num.copy())
            if node.left is None and node.right is None:
                ppp += judge(num)
            return ppp

        if root is not None:
            return keep_going(root, num)
