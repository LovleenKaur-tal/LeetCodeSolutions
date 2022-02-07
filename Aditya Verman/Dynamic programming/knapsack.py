# User function Template for python3

class Solution:

    # Function to return max value that can be put in knapsack of capacity W.

    def knapSack(self, W, wt, val, n):

        t = [[-1 for i in range(0, W + 1)] for j in range(0, n + 1)]

        for i in range(0, W + 1):
            t[0][i] = 0
        for j in range(0, n + 1):
            t[j][0] = 0
        for nn in range(1, n + 1):

            for ww in range(1, W + 1):
                if wt[nn - 1] <= ww:
                    t[nn][ww] = max(val[nn - 1] + t[nn - 1][ww - wt[nn - 1]], t[nn - 1][ww])
                elif wt[nn - 1] > ww:
                    t[nn][ww] = t[nn - 1][ww]
        return t[n][W]

        #     t[n-1] =  max((val[n-1]+self.knapSack(W-wt[n-1],wt,val,n-1)), self.knapSack(W,wt,val,n-1))
        #     return t[n-1]
        # elif wt[n-1]>W:
        #     t[n-1] = self.knapSack(W,wt,val,n-1)
        #     return t[n-1]

        # code here


# {
#  Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int, input().strip().split()))
        wt = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapSack(W, wt, val, n))
# } Driver Code Ends