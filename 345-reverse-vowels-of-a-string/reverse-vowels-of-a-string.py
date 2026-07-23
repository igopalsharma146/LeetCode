class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0 or len(s)==1:
            return s

        res=[]
        for ch in s:
            res.append(ch)

        left,right=0,len(res)-1
        vowel="aeiouAEIOU"
        while left < right:
            while left < right and res[left] not in vowel:
                left += 1
            while left < right and res[right] not in vowel:
                right -= 1 
            res[left],res[right]=res[right],res[left]
            left += 1
            right -=1
        return "".join(res)