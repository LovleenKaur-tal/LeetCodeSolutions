class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        r = 0
        length = len(nums)

        if sum(nums) < target:
            return 0
        while (l <= r and r < len(nums)):
            s = sum(nums[l:r + 1])
            if s < target:
                r = r + 1
            else:
                length = min(r - l + 1, length)
                l = l + 1

        return length
