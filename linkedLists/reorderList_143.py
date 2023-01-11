# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        self.dfs(head)

    def dfs(self, node: ListNode):
        if not node.next:
            return node
        old_next = node.next

        last_node = self.dfs(node.next)
        if node.next == last_node:
            node.next = None
        else:
            node.next = last_node
        



s = Solution()
l1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))


s.reorderList(l1)

dummy = l1
while dummy:
    print(f'{dummy.val}->', end='')
    dummy = dummy.next
print('null')