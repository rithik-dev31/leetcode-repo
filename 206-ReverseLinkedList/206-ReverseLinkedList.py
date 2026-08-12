# Last updated: 8/12/2026, 11:30:52 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        cur=head
        prev=None

        while cur:
            next_node=cur.next
            cur.next=prev
            prev=cur
            cur=next_node
        
        return prev


        