class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # n=len(s)
        # left,right=0,n-1
        # while left <= right:
        #     if ("a" <= s[left] <= "z") or ("A" <= s[left] <= "Z") or ("0" <= s[left] <= "9"):
        #         if ("a" <= s[right] <= "z") or ("A" <= s[right] <= "Z") or ("0" <= s[right] <= "9"):
        #             if s[left].lower()==s[right].lower():
        #                 left+=1
        #                 right-=1
        #                 continue
        #             else:
        #                 return False
        #         right-=1
        #         continue
        #     left+=1
        # return True


        left = 0
        right = len(s) - 1
        while left < right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True