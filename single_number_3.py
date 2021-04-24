class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        d = dict()

        for i in set(nums):
            d[i] = 0
        for num in nums:
            d[num] = d[num] + 1

        for k, v in d.items():
            if v == 1:
                result.append(k)
        return result



""""
Hashing method-17% faster
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        st = set(nums)
        for num in nums:
            xor=xor^num
        for num in st:
            if xor^num in st:
                return [xor^num, num]
"""
Bit manipulation : 30% faster
"""
