class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = 0
        charset = []
        result = 0
        for r in range(len(s)):

            while s[r] in charset:
                charset.pop(0)
                l = l + 1
            charset.append(s[r])
            result = max(result, (r - l) + 1)
        return result




