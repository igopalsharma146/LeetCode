# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res=[]
        curr=head
        while curr:
            res.append(curr.val)
            curr=curr.next

        # reversing the array
        def reverse(left,right):
            while left<=right:
                res[left],res[right]=res[right],res[left]
                left+=1
                right-=1

        left,right,n=0,k-1,len(res)
        while right<n:
            reverse(left,right)
            left=right+1
            right+=k

        curr1,i=head,0
        while curr1:
            curr1.val=res[i]
            curr1=curr1.next
            i+=1
        return head