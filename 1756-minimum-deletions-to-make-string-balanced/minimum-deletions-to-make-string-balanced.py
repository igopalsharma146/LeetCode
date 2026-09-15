class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0
        deletions = 0
        
        for ch in s:
            if ch == 'b':
                b_count += 1
            else:
                deletions = min(deletions + 1, b_count)
                print(deletions)
        return deletions

        # res = len(s)
        # a = 0
        # b = 0

        # for c in s:
        #     a += (c == 'a')

        # for c in s:
        #     a -= (c == 'a')
        #     res = min(res, a + b)
        #     b += (c == 'b')

        # return res
