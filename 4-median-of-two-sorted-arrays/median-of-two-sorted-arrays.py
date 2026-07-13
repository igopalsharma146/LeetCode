class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # n=len(nums1)
        # m=len(nums2)
        # merged=[]
        # i,j=0,0
        # while i<n and j<m:
        #     if nums1[i] < nums2[j]:
        #         merged.append(nums1[i])
        #         i+=1
        #     else:
        #         merged.append(nums2[j])
        #         j+=1
        
        # while i<n:
        #     merged.append(nums1[i])
        #     i+=1

        # while j<m:
        #     merged.append(nums2[j])
        #     j+=1

        # x=len(merged)
        # mid=x//2
        # if x%2 != 0:
        #     return float(merged[mid])
        # else:
        #     return (merged[mid-1] + merged[mid]) / 2.0


        # Another Solution
        merged=sorted(nums1+nums2)
        x=len(merged)
        mid=x//2
        if x%2 != 0:
            return float(merged[mid])
        else:
            return (merged[mid-1] + merged[mid]) / 2.0
