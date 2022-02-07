def LongestRepeatingSubsequence(self, str):
		# Code here
		m = len(str)
        n = len(str)

        t = [[-1 for i in range(0, n + 1)] for j in range(0, m + 1)]

        for i in range(0, n + 1):
            t[0][i] = 0
        for j in range(0, m + 1):
            t[j][0] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str[i - 1] == str[j - 1] and i!=j:
                    t[i][j] = 1 + t[i - 1][j - 1]
                else:
                    t[i][j] = max(t[i - 1][j], t[i][j - 1])
        return t[n][m]