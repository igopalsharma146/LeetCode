class Solution:
    import re
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub(r'[^a-z ]', ' ', paragraph)

        words = paragraph.split()

        freq={}
        for ch in words:
            freq[ch]=freq.get(ch,0)+1
        
        freq=dict(sorted(freq.items(), key=lambda x:x[1] , reverse=True))
        # print(freq)

        for key,val in freq.items():
            if key not in banned:
                return key