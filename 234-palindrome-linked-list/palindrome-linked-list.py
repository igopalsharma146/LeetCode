# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        curr=head
        res=[]
        while curr:
            res.append(curr.val)
            curr=curr.next

        left,right=0,len(res)-1
        while left <= right:
            if res[left] != res[right]:
                return False
            left += 1
            right -= 1
        return True