#1876. Substrings of Size Three with Distinct Characters

class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = 0
        r = 0
        window = 0

        d = dict()
        count = 0
        i = 0

        while (i < len(s) - 2):

            x = s[i]
            y = s[i + 1]
            z = s[i + 2]
            if x != y and x != z and y != z:
                count = count + 1

            i = i + 1
        return count
