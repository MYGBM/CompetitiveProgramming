# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        prev = None
        curr = head
        count = 0
        
        #finding middle which will be slow.val and reversing it
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
            if fast:
                count += 2
            else:
                count += 1
        
        if count % 2 != 0:
            second_half = slow
        else:
            second_half = slow.next

        start = prev

        while start and  second_half :
            if start.val != second_half.val:
                return False
            start=start.next
            second_half = second_half.next
        
        return True





     
        