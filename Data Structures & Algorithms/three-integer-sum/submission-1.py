class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()

        dct = collections.defaultdict(int)
        for idx, num in enumerate(nums):
            dct[num] = idx
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                lst_vl = -(nums[i] + nums[j])
                if (dct[lst_vl] > j):
                    ans.add((nums[i], nums[j], lst_vl))
        return list(ans)
        