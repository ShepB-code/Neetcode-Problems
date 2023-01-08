# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
            
        slow = head
        fast = head.next

        while fast and fast.next:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next

        return False

s = Solution()

l1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))

print(s.hasCycle(l1))

while dummy:
    print(f'{dummy.val}->', end='')
    dummy = dummy.next
print('null')


