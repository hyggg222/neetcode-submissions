class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:         
        dct = collections.defaultdict(int)
        ans = 0

        for num in nums:
            if not dct[num]:
                dct[num] = dct[num - 1] + dct[num + 1] + 1
                dct[num - dct[num - 1]] = dct[num]
                dct[num + dct[num + 1]] = dct[num]
                ans = max(ans, dct[num])

        return ans  