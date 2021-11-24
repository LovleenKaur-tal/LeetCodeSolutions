# User function Template for python3
class Solution:

    def count(self, arr, n, x):
        # code here

        l1 = 0
        r1 = n - 1
        first_idx = -1

        if x not in arr:
            return 0
        while (l1 <= r1 and r1 < n):
            mid = (l1 + r1) // 2

            if arr[mid] == x:
                first_idx = mid
                r1 = mid - 1
            elif arr[mid] < x:
                l1 = mid + 1
            else:
                r1 = mid - 1

        l2 = 0
        r2 = n - 1
        last_idx = -1
        while (l2 <= r2 and r2 < n):
            mid = (l2 + r2) // 2

            if arr[mid] == x:
                last_idx = mid
                l2 = mid + 1
            elif arr[mid] < x:
                l2 = mid + 1
            else:
                r2 = mid - 1

        return (last_idx - first_idx) + 1


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends