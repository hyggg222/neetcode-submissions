class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):

            if (nums[i] > 0):
                break
            if (i > 0 and nums[i] == nums[i - 1]):
                continue

            cur_Tar = -(nums[i])
            j, z = i + 1, len(nums) - 1
            while j < z:
                cur_Sum = nums[j] + nums[z]
                if (cur_Sum == cur_Tar):
                    ans.append((nums[i], nums[j], nums[z]))
                    j += 1
                    z -= 1
                    while nums[j] == nums[j - 1] and j < z:
                        j += 1
                elif (cur_Sum < cur_Tar):
                    j += 1
                else:
                    z -= 1
        
        return ans