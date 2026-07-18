class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """

        f = Counter(text)
        return min(f["b"], f["a"], f["l"] >> 1, f["o"] >> 1, f["n"])

        # b = a = l = o = n = 0
        # for c in text:
        #     if c == 'b':
        #         b += 1
        #     elif c == 'a':
        #         a += 1
        #     elif c == 'l':
        #         l += 1
        #     elif c == 'o':
        #         o += 1
        #     elif c == 'n':
        #         n += 1

        # return min(b, a, l // 2, o // 2, n)



        # # optimal
        # count = [0] * 26

        # for c in text:
        #     count[ord(c) - ord('a')] += 1

        # return min(
        #     count[ord('b') - ord('a')],
        #     count[ord('a') - ord('a')],
        #     count[ord('l') - ord('a')] // 2,
        #     count[ord('o') - ord('a')] // 2,
        #     count[ord('n') - ord('a')]
        # )