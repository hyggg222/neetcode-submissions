class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        dt = [0] * 26
        for char in s:
            dt[ord(char) - ord("a")] += 1
        for char in t:
            if dt[ord(char) - ord("a")] == 0:
                return False
            dt[ord(char) - ord("a")] -= 1
        return True