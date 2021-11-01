# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        l = 0
        r = 2 ** 31 - 1

        while (l <= r and r < 2 ** 31):
            mid = (l + r) // 2
            if reader.get(mid) == 2 ** 31 - 1:
                r = mid - 1
            else:
                l = mid + 1

        mx_val = r + 1
        l = 0
        while (l <= r and r < mx_val):

            mid = (l + r) // 2

            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1   

