class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2)

        t = [[-1 for i in range(0, n + 1)] for j in range(0, m + 1)]

        for i in range(0, n + 1):
            t[0][i] = 0
        for j in range(0, m + 1):
            t[j][0] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    t[i][j] = 1 + t[i - 1][j - 1]
                else:
                    t[i][j] = max(t[i - 1][j], t[i][j - 1])

        i = m
        j = n
        result = []
        while (i > 0 and j > 0):
            if text1[i - 1] == text2[j - 1]:
                result.append(text2[j - 1])
                i = i - 1
                j = j - 1
            else:
                if t[i][j - 1] >= t[i - 1][j]:
                    j = j - 1
                elif t[i][j - 1] < t[i - 1][j]:
                    i = i - 1
        print("Result", ''.join(sorted(result)))

        return t[m][n]

#         def func(m,n):

#             if m==0 or n==0:
#                 return 0


#             elif text1[m-1]==text2[n-1]:
#                 return 1+ func(m-1, n-1)
#             else:
#                 return max(func(m-1, n), func(m,n-1))

#         return func(m,n)

