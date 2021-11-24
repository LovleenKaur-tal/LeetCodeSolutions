class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        tmp = float('inf')
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while (l < r and r < len(nums)):
                summ = num + nums[l] + nums[r]
                if abs(tmp - target) > abs(target - summ):
                    tmp = summ
                if summ < target:
                    l = l + 1
                elif summ > target:
                    r = r - 1
                else:
                    return target

        return tmp
