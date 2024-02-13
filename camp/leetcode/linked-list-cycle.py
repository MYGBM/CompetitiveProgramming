# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        left = head
        right = head 

        while right != None and right.next!=None:
            right = right.next.next
            left = left.next

            if left == right:
                return True
        
        return False




        