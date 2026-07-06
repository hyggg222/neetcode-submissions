class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = []
        list_t = []
        for char in s:
            list_s.append(char)
        for char in t:
            list_t.append(char)
        list_t.sort()
        list_s.sort()
        return list_s == list_t
        