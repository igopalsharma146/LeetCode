# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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

        reverse(0,len(res)-1)

        curr1,i=head,0
        while curr1:
            curr1.val=res[i]
            curr1=curr1.next
            i+=1
        return head