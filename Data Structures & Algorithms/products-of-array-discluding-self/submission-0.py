class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, suf, ans = [0] * len(nums), [0] * len(nums), [0] * len(nums)
        pre[0] = nums[0]
        suf[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i]
        for i in range(len(nums) - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i]
        for i in range(0, len(nums)):
            if (i > 0 and i < len(nums) - 1):
                ans[i] = pre[i - 1] * suf[i + 1]
            elif (i > 0):
                ans[i] = pre[i - 1]
            else:
                ans[i] = suf[i + 1]

        return ans