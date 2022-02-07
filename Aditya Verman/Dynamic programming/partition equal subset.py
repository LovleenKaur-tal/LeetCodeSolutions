# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        # code here

        S = sum(arr)
        if S % 2 == 0:
            S = S // 2
        else:
            return 0

        t = [[0 for i in range(0, S + 1)] for j in range(0, N + 1)]

        for i in range(1, S + 1):
            t[0][i] = 0
        for j in range(0, N + 1):
            t[j][0] = 1

        for nn in range(1, N + 1):
            for ss in range(1, S + 1):

                if arr[nn - 1] <= ss:
                    t[nn][ss] = t[nn - 1][ss - arr[nn - 1]] or t[nn - 1][ss]
                else:
                    t[nn][ss] = t[nn - 1][ss]
        return t[N][S]


# {
#  Driver Code Starts
# Initial Template for Python3

import sys

input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])

        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends