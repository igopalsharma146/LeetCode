class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        f1 = {}
        for word in words:
            f1[word] = f1.get(word, 0) + 1

        sorted_dict = dict(sorted(f1.items(), key=lambda x: (-x[1], x[0])))

        res = []
        for key in sorted_dict:
            if len(res) == k:
                break
            res.append(key)
        return res