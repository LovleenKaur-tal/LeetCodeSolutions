class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = 0
        tmp = None
        if not nums:
            return

        while (r < len(nums)):
            if nums[r] == 0:
                r = r + 1
            else:
                tmp = nums[r]
                nums[r] = nums[l]
                nums[l] = tmp
                r = r + 1
                l = l + 1










