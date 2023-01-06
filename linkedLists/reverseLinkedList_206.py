from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        currNode = head
        prevNode = None

        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        
        return prevNode

s = Solution()
head = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
newHead = s.reverseList(head)

dummy = newHead
while dummy:
    print(f'{dummy.val}->', end='')
    dummy = dummy.next
print('null')