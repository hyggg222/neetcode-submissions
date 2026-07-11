class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, ans = 0, 0, 0
        dct = defaultdict(lambda: -1)
        while j < len(s):
            if dct[s[j]] != -1:
                i = max(i, dct[s[j]] + 1)
            ans = max(ans, j - i + 1)
            dct[s[j]] = j
            # print(f'valid {i} {j}')
            j += 1
        return ans