class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res=[]
        # wl=word length or tl=total length
        wl = len(words[0])
        tl = wl * len(words)

        target = {}
        for w in words:
            target[w] = target.get(w, 0) + 1

        for i in range(len(s) - tl + 1):
            window = s[i:i+tl]

            result = {}
            for j in range(0, tl, wl):
                w = window[j:j+wl]
                result[w] = result.get(w, 0) + 1

            if result == target:
                res.append(i)
        return res