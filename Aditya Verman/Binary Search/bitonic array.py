# User function Template for python3
class Solution:

    def findMaximum(self, arr, n):

        l = 0
        r = n - 1

        while (l <= r):

            mid = (l + r) // 2
            prev = (mid - n - 1) % n
            nxt = (mid + 1) % n
            if arr[mid] >= arr[prev] and arr[mid] >= arr[nxt]:
                return arr[mid]
            elif arr[prev] > arr[mid]:
                r = mid - 1
            elif arr[nxt] > arr[mid]:
                l = mid + 1
            elif mid == 0:
                if arr[0] > arr[1]:
                    return arr[0]
                else:
                    return arr[1]
            elif mid == n - 1:
                if arr[n - 1] > arr[n - 2]:
                    return arr[n - 1]
                else:
                    return arr[n - 2]
        return -1

    # code here


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends