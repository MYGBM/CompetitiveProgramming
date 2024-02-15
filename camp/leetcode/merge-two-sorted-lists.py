# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                temp = list1.next
                current.next = list1
                list1 = temp
                current = current.next

            else:
                temp = list2.next
                current.next = list2
                list2 = temp
                current = current.next
                
        if list1:
            current.next = list1
        if list2:
            current.next = list2
            
        
        return dummy.next

        