class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        d = dict()
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        count = 0
        if k == 0:
            for num in d:
                if d[num] > 1:
                    count = count + 1
        else:
            for num in d:
                if num + k in d:
                    count = count + 1
        return count




