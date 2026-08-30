# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        arr=[]
        curr=node.next
        while curr:
            arr.append(curr.val)
            curr=curr.next

        curr,i=node,0
        prev=None
        while i<len(arr):
            curr.val=arr[i]
            prev=curr
            curr=curr.next
            i+=1
        prev.next=None
        
