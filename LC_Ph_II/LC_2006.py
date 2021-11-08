from collections import defaultdict


class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        h = defaultdict(int)
        h[nums[0]] = 1
        res = 0
        for i in range(1, len(nums)):
            h[nums[i]] += 1
        count = 0
        for i, j in h.items():
            if i == 0:
                continue
            else:
                count = count + (h[i] * h[i - k])

        return count



