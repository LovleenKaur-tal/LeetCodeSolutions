from collections import OrderedDict


class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        d = OrderedDict()
        l = []
        for val in arr:
            d[val] = 0

        for i, num in enumerate(arr):
            d[num] = d[num] + 1

        for i, num in d.items():

            if num == 1:
                l.append(i)

        if len(l) < k - 1:
            return ""
        else:
            return l[k - 1]








