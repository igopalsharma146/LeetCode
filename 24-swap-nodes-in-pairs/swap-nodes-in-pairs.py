# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # if not head:
        #     return

        # if not head.next:
        #     return head
        
        # curr=head
        # slow=curr
        # fast=curr.next
        # while slow and fast:
        #     slow.val,fast.val=fast.val,slow.val
        #     if fast.next:
        #         slow = slow.next.next
        #         fast = fast.next.next
        #     else:
        #         break
        # return head

        curr = head
        while curr and curr.next:
            curr.val, curr.next.val = curr.next.val, curr.val
            curr = curr.next.next
        return head