class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def mini(i):
            n=len(nums)
            mini=float("inf")
            maxi=float("-inf")
            k=0
            while k < i+1:
                maxi=max(maxi,nums[k])
                k+=1
            while i<n:
                mini=min(mini,nums[i])
                i+=1
            return [maxi,mini]
        
        ind=-1
        for i in range(0,len(nums)):
            res = mini(i)
            maxi=res[0]
            minii=res[1]
            if maxi-minii <=k:
                return i
        return ind