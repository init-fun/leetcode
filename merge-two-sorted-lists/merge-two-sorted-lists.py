# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_list = ListNode()
        new_list_head = new_list
        
        while l1 and l2:
            if l1.val <= l2.val:
                new_list_head.next = ListNode(l1.val)
                l1 = l1.next
                
            else:
                new_list_head.next = ListNode(l2.val)
                l2 = l2.next
​
            new_list_head = new_list_head.next
            
        while l1:
            new_list_head.next = ListNode(l1.val)
            l1 = l1.next
            new_list_head = new_list_head.next
                
        
        while l2:
            new_list_head.next = ListNode(l2.val)
            l2 = l2.next
            new_list_head = new_list_head.next
            
        return new_list.next
