# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        d1=ListNode(0)
        d2=ListNode(0)
        curr=head
        curr1,curr2=d1,d2
        while curr:
            d=curr.next
            curr.next=None
            if curr.val < x:
                d1.next=curr
                d1=d1.next
            else:
                d2.next=curr
                d2=d2.next
            curr=d
        d1.next=curr2.next
        return curr1.next
