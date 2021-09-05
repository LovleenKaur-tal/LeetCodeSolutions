class Solution:
    def maxArea(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1
        max_area = 0
        while (l < r):

            width = (r - l)
            ht = min(height[r], height[l])

            area = width * ht

            max_area = max(area, max_area)

            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
        return max_area
