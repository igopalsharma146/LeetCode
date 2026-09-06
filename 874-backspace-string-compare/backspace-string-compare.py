class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        string = []
        for i in range(len(s)):
            if s[i] == "#":
                if string:
                    string.pop()
            else:
                string.append(s[i])

        str_sec = []
        for i in range(len(t)):
            if t[i] == "#":
                if str_sec:
                    str_sec.pop()
            else:
                str_sec.append(t[i])
        return string == str_sec