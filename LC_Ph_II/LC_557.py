class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        lst = s.split(" ")
        result = []

        for l in lst:
            result.append(l[::-1])
        return ' '.join(result)

