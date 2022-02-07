class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        n = len(nums)
        r = n - 1

        # no rotation
        if nums[l] < nums[r]:
            return nums[0]

        while l <= r:
            mid = l + (r - l) // 2
            left = (mid + n - 1) % n
            right = (mid + 1) % n

            if nums[mid] <= nums[left] and nums[mid] <= nums[right]:
                return nums[mid]
            elif nums[0] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1




