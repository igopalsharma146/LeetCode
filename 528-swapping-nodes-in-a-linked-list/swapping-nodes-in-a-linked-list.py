# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Brute force solution
        # res=[]
        # curr=head
        # while curr:
        #     res.append(curr.val)
        #     curr=curr.next

        # # reversing the array
        # def reverse(left,right):
        #     res[left],res[right]=res[right],res[left]

        # reverse(k-1,len(res)-k)

        # curr1,i=head,0
        # while curr1:
        #     curr1.val=res[i]
        #     curr1=curr1.next
        #     i+=1
        # return head

        # optimal solution
        curr = head
        for _ in range(k - 1):
            curr = curr.next
        
        node1 = curr
        curr = curr.next
        node2 = head
        while curr:
            node2 = node2.next
            curr = curr.next
        
        node1.val, node2.val = node2.val, node1.val
        
        return head