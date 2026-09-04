class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        right = list(nums)
        left = list(nums)
        for x in range(1,len(nums)):
            right[x] = max(right[x],right[x-1])
        for x in range(len(nums)-2,-1,-1):
            left[x] = min(left[x],left[x+1])
        print(right,left)
        for x in range(len(nums)):
            score = right[x]-left[x]
            if score <= k:
                return x
        return -1


        # def mini(i):
        #     n=len(nums)
        #     mini=float("inf")
        #     maxi=float("-inf")
        #     k=0
        #     while k < i+1:
        #         maxi=max(maxi,nums[k])
        #         k+=1
        #     while i<n:
        #         mini=min(mini,nums[i])
        #         i+=1
        #     return [maxi,mini]
        
        # ind=-1
        # for i in range(0,len(nums)):
        #     res = mini(i)
        #     maxi=res[0]
        #     minii=res[1]
        #     if maxi-minii <=k:
        #         return i
        # return ind