class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mini=float("inf")
        maxi=float("-inf")
        for val in nums:
            mini=min(mini,val)
            maxi=max(maxi,val)
        
        res=set(nums)
        ans=[]
        for i in range(mini,maxi+1):
            if i not in res:
                ans.append(i)
        return ans