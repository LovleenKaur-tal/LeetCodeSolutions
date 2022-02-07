def count_till_idx(i):
    count = 0
    j = 0
    while (j < i):
        if arr[j] == 0:
            count = count + 1
        j = j + 1
    return count


t = [[0 for i in range(0, sum + 1)] for j in range(0, len(arr) + 1)]
mod = pow(10, 9) + 7
for i in range(1, sum + 1):
    t[0][i] = 0
for j in range(0, n + 1):
    t[j][0] = pow(2, count_till_idx(j))

for nn in range(1, n + 1):
    for ss in range(1, sum + 1):
        if arr[nn - 1] <= ss:
            t[nn][ss] = (t[nn - 1][ss - arr[nn - 1]] % mod + t[nn - 1][ss] % mod) % mod
        else:
            t[nn][ss] = t[nn - 1][ss] % mod

return t[n][sum] % mod