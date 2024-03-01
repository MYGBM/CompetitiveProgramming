# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        array = []
        node = head
        n = 0
        curr = head

        #length of linked list
        while node:
            n += 1
            node = node.next
        
        remainder = n%k
        equal = n//k
        #making k partitions
        for part in range(k):

            #calculate length of partition
            if part< remainder:
                length = equal+1
            else:
                length = equal
            
            #traversing linked list partition
            #need to create a dummyNode
            dummy = ListNode()
            dummy_tail = dummy
            for i in range(length):
                if curr:
                    dummy_tail.next = curr
                    curr = curr.next
                    dummy_tail = dummy_tail.next
            dummy_tail.next = None
            array.append(dummy.next)
        
        return array





        