class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1={}
        for ch in s:
            d1[ch]=d1.get(ch,0)+1
        
        d2={}
        for ch in t:
            d2[ch]=d2.get(ch,0)+1
        
        if d1 == d2:
            return True
        else:
            return False

        # if len(s) != len(t):
        #     return False
        
        # freq = [0] * 26
        # for i in range(len(s)):
        #     freq[ord(s[i]) - ord('a')] += 1
        #     freq[ord(t[i]) - ord('a')] -= 1
        
        # for i in range(len(freq)):
        #     if freq[i] != 0:
        #         return False
        
        # return True