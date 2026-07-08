class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0

        for num in num_set:
            if (num - 1) in num_set: 
                continue
            cur_num = num
            cur_streak = 1
            while (cur_num + 1) in num_set:
                cur_streak += 1
                cur_num += 1
            ans = max(ans, cur_streak)
        
        return ans