class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        mx_len = 0
        res = ""
        for i in range(len(s)):

            # oddy
            l = i
            r = i

            while (l >= 0 and r < len(s) and s[l] == s[r]):

                if r - l + 1 > mx_len:
                    mx_len = r - l + 1
                    res = s[l:r + 1]

                l = l - 1
                r = r + 1

            # Eveny
            l = i
            r = i + 1

            while (l >= 0 and r < len(s) and s[l] == s[r]):
                if (r - l + 1) > mx_len:
                    mx_len = r - l + 1
                    res = s[l:r + 1]

                l = l - 1
                r = r + 1
        return res





