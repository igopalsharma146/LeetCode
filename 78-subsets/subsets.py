class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        def recursion(ind,subset):
            if ind>=len(nums):
                res.append(subset[:])
                return
            subset.append(nums[ind])
            recursion(ind+1,subset)
            subset.pop()
            recursion(ind+1,subset)
        recursion(0,[])
        return res