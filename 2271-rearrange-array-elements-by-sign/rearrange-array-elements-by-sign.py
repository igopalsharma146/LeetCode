class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[0]*len(nums)
        pos=0
        neg=1
        for num in nums:
            if num>0:
                res[pos]=num
                pos+=2
            else:
                res[neg]=num
                neg+=2
        return res


        # pos=[]
        # neg=[]
        # for ch in nums:
        #     if ch<0:
        #         neg.append(ch)
        #     else:
        #         pos.append(ch)
        
        # res=[]
        # i=0
        # while i<len(pos):
        #     res.extend([pos[i],neg[i]])
        #     i+=1
        # return res
