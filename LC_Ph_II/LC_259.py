class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        nums = sorted(nums)
        if not nums:
            return 0
        for i, num in enumerate(nums):
            l = i + 1
            r = len(nums) - 1

            while (l < r and r < len(nums)):
                summ = num + nums[l] + nums[r]

                if summ >= target:
                    r = r - 1
                elif summ < target:
                    count = count + (r - l)
                    l = l + 1

        return count

