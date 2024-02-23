# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(curr,val):
            if not curr:
                return 

            else:
                if val < curr.val:
                    return search(curr.left,val)

                elif val > curr.val:
                    return search(curr.right,val)
                else:
                    return curr
        return search(root,val)
            

                


