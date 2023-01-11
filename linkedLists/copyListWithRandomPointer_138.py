
# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # copy list structure without random
        hashmap = {}
        
        dummy = head

        
        while dummy:
            newList = Node(head)