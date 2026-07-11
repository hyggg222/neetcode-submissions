class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, ans = 0, 0, 0
        se = set()
        while j < len(s):
            if s[j] in se:
                while (s[j] in se):
                    se.remove(s[i])
                    i += 1
            se.add(s[j])
            # print(f'Valid {i} {j}')
            # print(' '.join(num for num in se))
            ans = max(ans, j - i + 1)
            j += 1
        return ans