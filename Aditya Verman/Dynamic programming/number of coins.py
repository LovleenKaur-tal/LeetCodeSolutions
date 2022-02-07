# User function Template for python3
class Solution:
    def minCoins(self, coins, M, V):
        # code here

        t = [[0 for i in range(0, V + 1)] for j in range(0, M + 1)]

        for i in range(0, V + 1):
            t[0][i] = float("inf")
        for i in range(1, M + 1):
            t[i][0] = 0
        for i in range(1, V + 1):
            if i % coins[0] == 0:
                t[1][i] = i / coins[0]
            else:
                t[1][i] = float("inf")
        for i in range(1, M + 1):
            for j in range(1, V + 1):

                if coins[i - 1] <= j:
                    t[i][j] = min(1 + t[i][j - coins[i - 1]], t[i - 1][j])
                else:
                    t[i][j] = t[i - 1][j]
        if t[M][V] == float("inf"):
            return -1
        return t[M][V]


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        v, m = input().split()
        v, m = int(v), int(m)
        coins = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minCoins(coins, m, v)
        print(ans)

# } Driver Code Ends