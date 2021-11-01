class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l = 0
        r = len(nums) - 1

        if target not in nums: return -1

        while (l >= 0 and r < len(nums)):

            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1

            else:
                r = mid - 1
        return -1

