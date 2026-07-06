class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for Str in strs:
            res = res + str(len(Str)) + "#"
            res = res + Str
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            S = ""
            len_num = 1
            for j in range(i, len(s)):
                if (s[j] == "#"):
                    break
                S = S + s[j]
                len_num += 1
            len_str = int(S)
            res.append(s[i + len_num : i + len_num + len_str])
            i = i + len_num + len_str
        return res