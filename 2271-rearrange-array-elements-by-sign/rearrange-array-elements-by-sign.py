class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos=[]
        neg=[]
        for ch in nums:
            if ch<0:
                neg.append(ch)
            else:
                pos.append(ch)
        
        res=[]
        i=0
        while i<len(pos):
            res.extend([pos[i],neg[i]])
            i+=1
        return res
