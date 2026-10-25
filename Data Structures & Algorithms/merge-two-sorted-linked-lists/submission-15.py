# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        bingo = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                bingo.next = list1
                list1 = list1.next
                bingo = bingo.next
            else :
                bingo.next = list2
                list2 = list2.next
                bingo = bingo.next

        bingo.next = list1 if list1 else list2
        return dummy.next









