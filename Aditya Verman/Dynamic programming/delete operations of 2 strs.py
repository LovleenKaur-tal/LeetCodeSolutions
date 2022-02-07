class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)

        t = [[-1 for i in range(0, n + 1)] for j in range(0, m + 1)]

        for i in range(0, n + 1):
            t[0][i] = 0
        for j in range(0, m + 1):
            t[j][0] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    t[i][j] = 1 + t[i - 1][j - 1]
                else:
                    t[i][j] = max(t[i - 1][j], t[i][j - 1])

        i = m
        j = n
        result = []
        while (i > 0 and j > 0):
            if word1[i - 1] == word2[j - 1]:
                result.append(word2[j - 1])
                i = i - 1
                j = j - 1
            else:
                if t[i][j - 1] >= t[i - 1][j]:
                    j = j - 1
                elif t[i][j - 1] < t[i - 1][j]:
                    i = i - 1
        l1 = list(word1)
        l2 = list(word2)
        print("Result", l1)
        d1 = dict()

        d2 = dict()

        for l in l1:
            if l not in d1:
                d1[l] = 1
            else:
                d1[l] += 1
        for l in l2:
            if l not in d2:
                d2[l] = 1
            else:
                d2[l] += 1
        for l in result:
            if l in d1:
                d1[l] -= 1
            if l in d2:
                d2[l] -= 1

        summ = sum(d1.values()) + sum(d2.values())

        return summ

