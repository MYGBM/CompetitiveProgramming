# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.curr = 0
        def range_sum(node):
            if not node:
                return 0
            if low<=node.val<=high:
                self.curr+=node.val
            range_sum(node.left)
            range_sum(node.right)
        
        range_sum(root)
        return self.curr

        