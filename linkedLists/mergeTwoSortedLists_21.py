from typing import Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # choose a head
        if list1.val < list2.val:
            newList = list1
            list1 = list1.next
        else:
            newList = list2
            list2 = list2.next
        returnHead = newList
        # add elements to newList
        while list1 and list2:
            if list1.val < list2.val:
                newList.next = list1
                list1 = list1.next
            else:
                newList.next = list2
                list2 = list2.next
            
            newList = newList.next
        
        # add any remaining elements from list1
        while list1:
            newList.next = list1
            newList = newList.next
            list1 = list1.next
        
        # add any remaining elements from list2
        while list2:
            newList.next = list2
            newList = newList.next
            list2 = list2.next
        
        return returnHead

s = Solution()
l1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
l2 = ListNode(1, ListNode(3, ListNode(4, ListNode(5))))

newList = s.mergeTwoLists(l1, l2)

dummy = newList
while dummy:
    print(f'{dummy.val}->', end='')
    dummy = dummy.next
print('null')