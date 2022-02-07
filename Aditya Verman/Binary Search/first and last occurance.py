# User function Template for python3
class Solution:
    def firstAndLast(self, arr, n, x):
        # Code here
        l = 0
        r = n - 1
        result = []
        first = None
        while (l <= r and r < n):

            m = (l + r) // 2
            if arr[m] == x:
                first = m
                r = m - 1
            elif x > arr[m]:
                l = m + 1
            else:
                r = m - 1
        out = [-1]

        if first != None:
            last = first
            while (last < len(arr) and arr[last] == arr[first]):
                last = last + 1

            out = [first, last - 1]
        return out


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, x = [int(i) for i in input().split()]
        arr = [int(i) for i in input().split()]
        ob = Solution()
        ans = ob.firstAndLast(arr, n, x)
        s = (" ").join(map(str, ans))
        print(s)

# } Driver Code Ends