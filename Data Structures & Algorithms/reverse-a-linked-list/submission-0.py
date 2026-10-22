# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # print(head.next.next.val)
        
        if not head:
            return None
        newHead = head
        if head.next != None:
            newHead = self.reverseList(head = head.next)
            head.next.next = head
        head.next = None
        return newHead
            
        # if head:
        #     print("This works")
        # if head and head.next != None:
        #     print(head.val)
        #     print("NXT: ",head.next.val)
        #     print("---->")
        #     self.reverseList(head = head.next)
        # else:
        #     print(head.val)
        #     print("<---LAST NODE---")


        