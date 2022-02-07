# User function Template for python3
class Solution:

    def search(self, pat, txt):
        # code here

        d = dict()
        for i in pat:
            if i not in d:
                d[i] = 1
            else:
                d[i] = d[i] + 1

        l = 0
        r = 0
        d2 = dict()
        ws = len(pat)
        count = 0
        while (r < len(txt)):

            if txt[r] not in d2:
                d2[txt[r]] = 1
            else:
                d2[txt[r]] = d2[txt[r]] + 1

            if r - l + 1 < ws:
                r = r + 1
                continue
            else:
                if d == d2:
                    count = count + 1

            d2[txt[l]] = d2[txt[l]] - 1
            if not d2[txt[l]]:
                d2.pop(txt[l], None)
            l = l + 1
            r = r + 1


return count
# {
#  Driver Code Starts
# Initial Template for Python 3


# Driver code
if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        txt = input().strip()
        pat = input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc = tc - 1
# } Driver Code Ends