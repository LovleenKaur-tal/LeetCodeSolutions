class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i, num in enumerate(nums):
            diff = target - num

            if diff not in map:
                map[num] = i

            else:
                return [map[diff], i]
        return [-1, -1]



# 98%