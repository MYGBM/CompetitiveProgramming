# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.dict= defaultdict(int)

        def mode(node):
            if not node:
                return 
            self.dict[node.val]+=1
            mode(node.left)
            mode(node.right)
        mode(root)
        maxii= max(self.dict.values())
        ans = []
        for key in self.dict:
            if self.dict[key]==maxii:
                ans.append(key)
        return ans


