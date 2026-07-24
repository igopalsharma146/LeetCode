class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=set()
        s1=set(nums2)
        for value in nums1:
            if value in s1:
                res.add(value)
        return list(res)

        # set1 = set(nums1)
        # set2 = set(nums2)
        # return list(set1.intersection(set2))