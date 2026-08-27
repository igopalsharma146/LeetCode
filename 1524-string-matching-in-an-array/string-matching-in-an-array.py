class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res=[]
        for ch in words:
            for ch1 in words:
                if ch==ch1:
                    continue
                if ch1 in ch:
                    if ch1 not in res:
                        res.append(ch1)
                    continue
        return res
