# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = head
        right = head

        while right.next != None:
            left = left.next
            right = right.next.next

            if right == None:
                return left
        return left

        