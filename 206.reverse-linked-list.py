# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        last_head = None
        while head.next != None:
            reverse_head = ListNode(val=head.val, next=last_head)
            last_head = reverse_head
            head = head.next

        return ListNode(val=head.val, next=last_head)
