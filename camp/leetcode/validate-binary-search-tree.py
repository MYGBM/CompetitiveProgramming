# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans = []
        def valid(node):
            if not node:
                return None
            valid(node.left)
            self.ans.append(node.val)
            valid(node.right)
        valid(root)
        if sorted(self.ans) == self.ans and len(set(self.ans))== len(self.ans):
            return True
        return False
        