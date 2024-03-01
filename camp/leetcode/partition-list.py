# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = ListNode()
        after = ListNode()
        before_tail = before
        after_tail = after
        curr = head

        while curr:
            if curr.val <x:
                before_tail.next = curr
                before_tail = before_tail.next
            elif curr.val >=x:
                after_tail.next = curr
                after_tail = after_tail.next
            curr=curr.next

        after_tail.next = None
        before_tail.next = after.next
        return before.next

        
        

        