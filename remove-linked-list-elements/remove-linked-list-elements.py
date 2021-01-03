# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        tmp_node = ListNode()
        tmp_node.next = head
        
        cur, prev_node = head,tmp_node 
        while cur:
            if cur.val == val:
                prev_node.next = cur.next
            else:
                prev_node = cur
                
            cur = cur.next
        return tmp_node.next
                
                
        
        
