class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1

        while (l <= r and r < len(s) and l >= 0):
            tmp = s[r]
            s[r] = s[l]
            s[l] = tmp

            l = l + 1
            r = r - 1


