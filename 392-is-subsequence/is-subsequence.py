class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i=0
        for ch in t:
            if i<len(s) and ch==s[i] :
                i+=1
        if i==len(s):
            return True
        else:
            return False