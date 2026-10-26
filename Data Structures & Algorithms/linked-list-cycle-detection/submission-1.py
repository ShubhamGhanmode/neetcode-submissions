# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        tail = head
        while tail and tail.next != None:
            if tail.val not in seen:
                seen.add(tail.val)
                tail = tail.next
            else:
                return True
        return False
        