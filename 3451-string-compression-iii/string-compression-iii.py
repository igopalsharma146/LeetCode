class Solution:
    def compressedString(self, word: str) -> str:
        res = []
        cur = word[0]
        count = 0
        for ch in word + '!':
            if ch != cur or count >= 9:
                res.append(str(count))
                res.append(cur)
                count = 0
                cur = ch
            count += 1
        return ''.join(res)

        # read,res=0,""
        # while read < len(word):
        #     char = word[read]
        #     count = 0

        #     # Count consecutive same characters
        #     while read < len(word) and word[read] == char:
        #         read += 1
        #         count += 1

        #     # writing count
        #     while count>9:
        #         res+=str(9)
        #         res+=char
        #         count-=9
        #     if count>0:
        #         res+=str(count)
        #         res+=char
        # return res