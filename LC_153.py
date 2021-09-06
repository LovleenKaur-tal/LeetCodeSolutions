class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        min_small = 5002

        while (l <= r):
            if nums[l] <= nums[r]:
                return min(min_small, nums[l])
                break
            mid = (l + r) // 2

            min_small = min(min_small, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return min_small




