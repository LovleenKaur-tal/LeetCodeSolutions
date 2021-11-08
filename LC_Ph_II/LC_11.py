class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        l = 0
        r = len(height) - 1
        max_water = -1

        while (l < r and l >= 0 and r < len(height)):
            max_water = max(max_water, (r - l) * min(height[r], height[l]))

            if height[l] <= height[r]:
                l = l + 1
            else:
                r = r - 1
        return max_water


