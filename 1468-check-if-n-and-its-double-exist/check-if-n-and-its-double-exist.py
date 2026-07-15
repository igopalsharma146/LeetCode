class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hash1=set()
        for i in range(0,len(arr)):
            if arr[i]*2 in hash1:
                return True
            if arr[i]%2==0 and arr[i]//2 in hash1:
                return True
            else:
                hash1.add(arr[i])
        return False