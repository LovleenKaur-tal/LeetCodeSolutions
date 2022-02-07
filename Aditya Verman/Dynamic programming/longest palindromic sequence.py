class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        m = len(s)
        x = s[::-1]
        n = len(x)

        t = [[-1 for i in range(0, n + 1)] for j in range(0, m + 1)]

        for i in range(0, n + 1):
            t[0][i] = 0
        for j in range(0, m + 1):
            t[j][0] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == x[j - 1]:
                    t[i][j] = 1 + t[i - 1][j - 1]
                else:
                    t[i][j] = max(t[i - 1][j], t[i][j - 1])

        return t[m][n]


