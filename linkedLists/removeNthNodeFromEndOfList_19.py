# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       
        dummy = head
        length = self.getLength(dummy)

        numToRemove = length - n

        dummy = head
        prev = None
        for _ in range(numToRemove):
            prev = dummy
            dummy = dummy.next
        
        if not prev:
            head = head.next
        else:
            prev.next = dummy.next
        return head

    def getLength(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length


s = Solution()
l1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))


s.removeNthFromEnd(l1, 5)

dummy = l1
while dummy:
    print(f'{dummy.val}->', end='')
    dummy = dummy.next
print('null')