class Solution(object):
    def findPeaks(self, mountain):
        """
        :type mountain: List[int]
        :rtype: List[int]
        """
        res=[]
        i=1
        while i<len(mountain)-1:
            if mountain[i-1] < mountain[i] > mountain[i+1]:
                res.append(i)
            i+=1
        return res