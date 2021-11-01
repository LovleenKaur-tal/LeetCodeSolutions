# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        bad_version = None
        while (l <= r and r < n + 1):

            mid = (l + r) // 2

            if isBadVersion(mid):
                bad_version = mid
                r = mid - 1
            else:
                l = mid + 1
        return bad_version





