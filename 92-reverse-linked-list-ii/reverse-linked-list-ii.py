# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """            
        arr=[]
        curr=head
        while curr:
            arr.append(curr.val)
            curr=curr.next

        left,right=left-1,right-1
        while left<=right:
                arr[left],arr[right]=arr[right],arr[left]
                left+=1
                right-=1

        curr,i=head,0
        while curr:
            curr.val=arr[i]
            curr=curr.next
            i+=1
        return head