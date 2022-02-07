class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        m = len(str1)
        n = len(str2)

        t = [[-1 for i in range(0, n + 1)] for j in range(0, m + 1)]

        for i in range(0, n + 1):
            t[0][i] = 0
        for j in range(0, m + 1):
            t[j][0] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    t[i][j] = 1 + t[i - 1][j - 1]
                else:
                    t[i][j] = max(t[i - 1][j], t[i][j - 1])

        lcs = t[m][n]

        i = m
        j = n
        result = []
        while (i > 0 and j > 0):
            if str1[i - 1] == str2[j - 1]:
                result.append(str2[j - 1])
                i = i - 1
                j = j - 1
            else:
                if t[i][j - 1] >= t[i - 1][j]:
                    result.append(str2[j - 1])
                    j = j - 1
                elif t[i][j - 1] < t[i - 1][j]:
                    result.append(str1[i - 1])
                    i = i - 1

        while (i > 0):
            result.append(str1[i - 1])
            i = i - 1
        while (j > 0):
            result.append(str2[j - 1])
            j = j - 1
        x = ''.join(result[::-1])

        return x


