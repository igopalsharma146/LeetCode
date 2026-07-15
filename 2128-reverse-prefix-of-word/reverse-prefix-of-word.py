class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch in word:
            chind = word.index(ch)
        else:
            return word
        s = word[:chind+1]
        s = s[::-1]
        return s+word[chind+1:]