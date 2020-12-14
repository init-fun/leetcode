# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # do a circle traversing both the list sequestially 
        # at some point they will meet
        ptr1 = headA
        ptr2 = headB
        while ptr1 != ptr2:
            if ptr1:
                ptr1 = ptr1.next
            else:
                ptr1 = headB
            if ptr2:
                ptr2 = ptr2.next
            else:
                ptr2 = headA
        return ptr1
