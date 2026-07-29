from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(list)
        for i in range(len(s)):
            freq[ord(s[i]) - ord("A")].append(i)
        ans = 0
        for i in range(26):
            if (len(freq[i]) == 0):
                continue
            ls = freq[i]
            S, res, l = k, 0, 0
            for r in range(1, len(ls)):
                S -= ls[r] - ls[r - 1] - 1
                while (l < r) and (S < 0):
                    S += ls[l + 1] - ls[l] - 1
                    l += 1
                if (l > 0):
                    ans = max(ans, ls[r] - ls[l] + 1)
                else:
                    ans = max(ans, ls[r] - ls[l] + 1 + min(S, ls[l]))
            if (l > 0):
                ans = max(ans, ls[len(ls) - 1] - ls[l] + 1 + min(S, (len(s) - 1) - ls[len(ls) - 1]))
            else:
                ans = max(ans, ls[len(ls) - 1] - ls[l] + 1 + min(S, (len(s) - 1) - ls[len(ls) - 1] + ls[l]))
        return ans