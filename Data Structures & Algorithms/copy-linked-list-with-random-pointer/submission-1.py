"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {}
        temp = head

        while temp:
            newNode = Node(temp.val, None, None)
            oldToNew[temp] = newNode
            temp = temp.next
        temp = head
        while temp:
            newHead = oldToNew[temp]
            oldNext = temp.next
            oldRandom = temp.random
            if oldNext:
                newNext = oldToNew[oldNext]
                newHead.next = newNext
            if oldRandom:
                newRandom = oldToNew[oldRandom]
                newHead.random = newRandom
            temp = temp.next
        return oldToNew[head] if head else None
