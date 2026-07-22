class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split()

        if len(pattern) != len(s):
            return False

        p_to_w = {}
        w_to_p = {}
        for ch, word in zip(pattern, s):

            if ch in p_to_w:
                if p_to_w[ch] != word:
                    return False
            else:
                p_to_w[ch] = word

            if word in w_to_p:
                if w_to_p[word] != ch:
                    return False
            else:
                w_to_p[word] = ch

        return True