# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        # ye wala code bilkul sahi h 
        # slow = fast = head
        # prev = None

        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow.next, prev, slow = prev, slow, slow.next

        # res = 0
        # while slow:
        #     res = max(res, prev.val + slow.val)
        #     prev, slow = prev.next, slow.next

        # return res

        #easy approch but memory consuming
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        left = 0
        right = len(arr) - 1

        ans = 0

        while left < right:
            ans = max(ans, arr[left] + arr[right])

            left += 1
            right -= 1

        return ans