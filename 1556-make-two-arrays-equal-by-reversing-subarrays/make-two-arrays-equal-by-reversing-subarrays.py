class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        # ye code run ho jayega per ye sahi tarika nahi h
        arr.sort()
        target.sort()
        if target==arr:
            return True
        return False


        # # sahi tarika karne ka
        # i=0
        # while i<len(target):
        #     # agar value sahi position me h to reverse karne ki need nahi h
        #     if target[i]==arr[i]:
        #         i+=1
        #         continue

        #     # finding the position of reversing array
        #     left=right=i
        #     while right<len(arr) and target[i]!=arr[right]:
        #         right+=1
            
        #     # agar target ka koi bhi ek element hame arr na mila to turant false return kar denge
        #     if right==len(arr):
        #         return False
            
        #     #Reversing the array
        #     while left<right:
        #         arr[left],arr[right]=arr[right],arr[left]
        #         left+=1
        #         right-=1
        #     i+=1
        
        # # checking both array
        # if target==arr:
        #     return True
        # return False
