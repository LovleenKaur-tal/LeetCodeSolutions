class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(nums) - 1

        if len(nums) == 1 and nums[0] == target:
            return [0, 0]

        first_occurence_idx = -1

        # First Occurence
        while (l <= r and r < len(nums)):

            mid = l + (r - l) / 2

            if target == nums[mid]:
                first_occurence_idx = mid
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        l2 = 0
        r2 = len(nums) - 1
        last_occurence_idx = -1
        # Last Occurence
        while (l2 <= r2 and r2 < len(nums)):

            mid = l2 + (r2 - l2) / 2

            if target == nums[mid]:
                last_occurence_idx = mid
                l2 = mid + 1
            elif target > nums[mid]:
                l2 = mid + 1
            else:
                r2 = mid - 1
        return [first_occurence_idx, last_occurence_idx]
