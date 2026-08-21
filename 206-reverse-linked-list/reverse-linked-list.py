# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # Brute force solution
        # res=[]
        # curr=head
        # while curr:
        #     res.append(curr.val)
        #     curr=curr.next

        # # reversing the array
        # def reverse(left,right):
        #     while left<=right:
        #         res[left],res[right]=res[right],res[left]
        #         left+=1
        #         right-=1

        # reverse(0,len(res)-1)

        # curr1,i=head,0
        # while curr1:
        #     curr1.val=res[i]
        #     curr1=curr1.next
        #     i+=1
        # return head

        # optimal solution
        if head is None or head.next is None:
            return head
        d=None
        temp=head
        while temp:
            x=temp.next
            temp.next=d
            d=temp
            temp=x
        return d     