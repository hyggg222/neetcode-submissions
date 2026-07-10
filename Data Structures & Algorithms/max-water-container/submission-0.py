class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                ans = max(ans, (j - i) * min(heights[i], heights[j]))
        return ans