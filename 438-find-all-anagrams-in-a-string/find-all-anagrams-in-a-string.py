class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        pmap = {}
        smap = {}

        for ch in p:
            pmap[ch] = pmap.get(ch, 0) + 1

        for ch in s[:len(p)]:
            smap[ch] = smap.get(ch, 0) + 1

        res = []
        if pmap == smap:
            res.append(0)

        left = 0
        for right in range(len(p), len(s)):
            smap[s[right]] = smap.get(s[right], 0) + 1

            smap[s[left]] -= 1
            if smap[s[left]] == 0:
                del smap[s[left]]

            left += 1
            if pmap == smap:
                res.append(left)

        return res


        # TLE ERROR
        # n=len(p)
        # res=[]
        # first="".join(sorted(p))
        # for i in range(0,len(s)):
        #     second="".join(sorted(s[i:i+n]))
        #     if first==second:
        #         res.append(i)
        # return res