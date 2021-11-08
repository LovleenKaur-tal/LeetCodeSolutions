class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while (l < r and l >= 0 and r < len(nums)):
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r = r - 1
                elif threeSum < 0:
                    l = l + 1
                else:
                    result.append([num, nums[l], nums[r]])
                    l = l + 1
                    while l < r and nums[l] == nums[l - 1]:
                        l = l + 1
        return result





