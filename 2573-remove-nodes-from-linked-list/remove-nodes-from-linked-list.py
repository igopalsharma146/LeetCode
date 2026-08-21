# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        res=[]
        curr=head
        while curr:
            res.append(curr.val)
            curr=curr.next

        stack=[]
        for ch in res:
            while stack and stack[-1]<ch:
                stack.pop()
            stack.append(ch)

        dummy=curr1=ListNode(0)
        for ch in stack:
            curr1.next=ListNode(ch)
            curr1=curr1.next
        return dummy.next