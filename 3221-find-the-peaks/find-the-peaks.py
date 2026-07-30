class Solution(object):
    def findPeaks(self, mountain):
        """
        :type mountain: List[int]
        :rtype: List[int]
        """
        res=[]
        i=1
        prev=mountain[0]
        while i<len(mountain)-1:
            if prev < mountain[i] > mountain[i+1]:
                res.append(i)
            prev=mountain[i]
            i+=1
        return res