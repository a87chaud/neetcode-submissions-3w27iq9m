# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        slow, fast = head, head
        i = 0
        while fast and i < n:
            fast = fast.next
            i += 1
        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        # slow is the node to remove
        if prev:
            temp = slow.next
            prev.next = slow.next
            slow.next = None
        else:
            return head.next
        return head