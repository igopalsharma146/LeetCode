# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
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

        left,right,n=0,0,len(res)
        i=2
        while right<n:
            if (right-left)%2==0:
                reverse(left+1,right)
            left=right
            right+=i
            i+=1
        if (n-left+1)%2==0:
            reverse(left+1,n-1)

        curr1,i=head,0
        while curr1:
            curr1.val=res[i]
            curr1=curr1.next
            i+=1
        return head