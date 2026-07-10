class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()

        for i in range(len(nums)):
            cur_Tar = -(nums[i])
            j, z = i + 1, len(nums) - 1
            while j < z:
                cur_Sum = nums[j] + nums[z]
                if (cur_Sum == cur_Tar):
                    ans.add((nums[i], nums[j], nums[z]))
                    j += 1
                elif (cur_Sum < cur_Tar):
                    j += 1
                else:
                    z -= 1
        
        return list(ans)