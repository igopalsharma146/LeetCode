# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        res=[]
        curr=head
        while curr:
            res.append(curr.val)
            curr=curr.next
        # print(res)

        # Re_arranging
        left,right=0,len(res)-1
        result=[]
        while left<=right:
            if left==right:
                result.append(res[left])
                break
            result.extend([res[left],res[right]])
            left+=1
            right-=1
        # print(result)

        curr=head
        i=0
        while curr:
            curr.val=result[i]
            curr=curr.next
            i+=1
