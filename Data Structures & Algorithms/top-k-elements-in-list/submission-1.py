class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        ls = []
        for key, value in freq.items():
            ls.append([value, key])
        ls.sort(reverse = True)
        ans = []
        for i in range(0, min(k, len(ls))):
            ans.append(ls[i][1])
        return ans