# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even_dummy = ListNode()
        odd_dummy = ListNode()

        even_tail = even_dummy
        odd_tail = odd_dummy

        count = 1
        curr = head

        while curr:
            if count%2!=0:
                odd_tail.next = curr
                odd_tail = odd_tail.next
                # odd_tail.next = None
            elif count%2==0:
                even_tail.next = curr
                even_tail =even_tail.next
                # even_tail.next = None
            count+=1
            curr=curr.next

        odd_tail.next = even_dummy.next
        even_tail.next = None
        return odd_dummy.next


        

                








        