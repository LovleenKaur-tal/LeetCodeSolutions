# User function Template for python3
class Solution:
    def minDifference(self, arr, n):

    # code here

    s1 = []
    if n == 1:
        return arr[0]

    def findsubset(arr):
        N = n
        S = sum(arr)

        t = [[0 for i in range(0, S + 1)] for j in range(0, N + 1)]

        for nn in range(0, N + 1):
            t[nn][0] = 1
        for ss in range(1, S + 1):
            t[0][ss] = 0

        for nn in range(1, N + 1):
            for ss in range(1, S + 1):

                if arr[nn - 1] <= ss:
                    t[nn][ss] = t[nn - 1][ss - arr[nn - 1]] or t[nn - 1][ss]
                else:
                    t[nn][ss] = t[nn - 1][ss]
        return t

    result = []
    d = findsubset(arr)
    for i in range(1, len(d[0])):
        if d[n][i]:
            result.append(i)

    min_so_far = float("inf")
    max_range = sum(arr)

    for i in range(0, len(result) // 2):
        s1 = result[i]

        min_so_far = min(min_so_far, max_range - (2 * s1))

    return min_so_far


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minDifference(arr, N)
        print(ans)

# } Driver Code Ends