class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        idx = None

        while (l <= r and r < len(nums)):

            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                idx = mid + 1
                l = mid + 1
            else:
                idx = mid - 1
                r = mid - 1
        return l
