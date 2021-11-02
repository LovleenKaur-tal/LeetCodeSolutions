class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        l = 0
        r = len(nums) - 1
        result = list()

        while (l >= 0 and l <= r):
            if (nums[l] * nums[l] >= nums[r] * nums[r]):
                result.append(nums[l] * nums[l])
                l = l + 1
            else:
                result.append(nums[r] * nums[r])
                r = r - 1
        return result[::-1]


