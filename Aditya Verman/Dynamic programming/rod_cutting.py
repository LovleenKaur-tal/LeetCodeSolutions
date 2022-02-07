class Solution:
    def cutRod(self, price, n):
        # code here
        size = len(price)

        length = [i for i in range(1, n + 1)]
        t = [[0 for i in range(0, n + 1)] for j in range(0, size + 1)]

        for i in range(1, n + 1):
            t[0][i] = 0
        for j in range(0, size + 1):
            t[i][0] = 0

        for i in range(1, size + 1):
            for j in range(1, n + 1):
                if length[i - 1] <= j:
                    t[i][j] = max(price[i - 1] + t[i][j - length[i - 1]], t[i - 1][j])
                else:
                    t[i][j] = t[i - 1][j]

        return t[n][size]
