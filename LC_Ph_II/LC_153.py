class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        n = len(nums)
        if len(nums) > 2:
            while (l <= r):

                mid = (l + r) // 2

                # Find unsorted
                prev_idx = (mid + n - 1) % n
                next_idx = (mid + 1) % n

                if nums[mid] < (nums[next_idx]) and nums[mid] < (nums[prev_idx]):
                    return nums[mid]


                elif nums[mid] < nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[1]
            else:
                return nums[0]
        elif len(nums) == 1:
            return nums[0]
        else:
            return nums




