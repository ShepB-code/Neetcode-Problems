# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        l3 = ListNode()
        keep = l3
        
        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            num3 = num1 + num2 + carry
        
            l3.val = (num3 % 10)
            carry = num3 // 10
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if l1 or l2 or carry:
                l3.next = ListNode()
            l3 = l3.next

        return keep



s = Solution()

num1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
num2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9)))) 


res = s.addTwoNumbers(num1, num2)

dummy = res
while dummy:
    print(f'{dummy.val}->', end='')
    dummy = dummy.next
print('null')