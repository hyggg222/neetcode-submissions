class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            if (dct.get(target - nums[i], -1) != -1):
                return [dct[target - nums[i]], i]
            dct[nums[i]] = i