

def isSubsetSum(self, N, arr, sum):
    t = [[0 for i in range(0, sum + 1)] for j in range(0, N + 1)]

    for nn in range(0, N + 1):
        t[nn][0] = 1
    for ss in range(1, sum + 1):
        t[0][ss] = 0

    for nn in range(1, N + 1):
        for ss in range(1, sum + 1):

            if arr[nn - 1] <= ss:
                t[nn][ss] = t[nn - 1][ss - arr[nn - 1]] or t[nn - 1][ss - 1]
            else:
                t[nn][ss] = t[nn - 1][ss - 1]
    return t[nn][ss]
