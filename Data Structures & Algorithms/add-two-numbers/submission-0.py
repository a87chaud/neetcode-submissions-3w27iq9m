# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(val=-1)
        tail = newHead
        carry = 0
        while l1 or l2:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            currSum = l1Val + l2Val + carry
            carry = currSum // 10
            remainder = currSum % 10
            tail.next = ListNode(val=remainder)
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry > 0:
            tail.next = ListNode(val=carry)
            tail = tail.next
        return newHead.next