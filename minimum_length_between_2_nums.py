import sys


class Solution:
    def minDist(self, arr, n, x, y):
        prev = None
        ind = None
        min_dist = sys.maxsize
        for idx, num in enumerate(arr):
            if num in [x, y]:
                prev = idx
                break
        if prev is None:
            return -1
        if x not in arr or y not in arr:
            return -1
        i = prev
        while (i < len(arr)):
            if arr[i] == x or arr[i] == y:
                if arr[prev] != arr[i] and i - prev < min_dist:
                    min_dist = i - prev
                prev = i
            i = i + 1

        return min_dist


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x, y = list(map(int, input().strip().split()))
        print(Solution().minDist(arr, n, x, y))

# } Driver Code Ends