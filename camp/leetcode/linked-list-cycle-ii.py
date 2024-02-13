# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = head
        right = head 
        second_left = head

        while right != None and right.next!=None:
            right = right.next.next
            left = left.next

            if left == right:
                intersection = left
                while True:
                    if intersection == second_left:
                        return intersection
                    intersection = intersection.next
                    second_left = second_left.next

                    
        
        return None
        