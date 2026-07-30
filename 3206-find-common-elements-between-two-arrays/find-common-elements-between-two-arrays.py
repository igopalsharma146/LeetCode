class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        count=0
        s1=set(nums1)
        s2=set(nums2)

        for ch in nums1:
            if ch in s2:
                count+=1
        res.append(count)

        count=0
        for ch in nums2:
            if ch in s1:
                count+=1
        res.append(count)
        return res