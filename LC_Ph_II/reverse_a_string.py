class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        while (l < r and r < len(s)):
            tmp = s[l]
            s[l] = s[r]
            s[r] = tmp

            l = l + 1
            r = r - 1

