# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashMapA = {}
        hashMapB = {}

        
        currA = headA
        while currA:
            hashMapA[currA] = currA.next
            currA = currA.next
        
        currB = headB
        while currB:
            hashMapB[currB] = currB.next
            currB= currB.next

        for node in hashMapA:
            if node in hashMapB:
                if hashMapB[node] == hashMapA[node]:
                    return node
        else:
            return None
    

        