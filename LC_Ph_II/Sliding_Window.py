# User function Template for python3
class Solution:

    def search(self, pat, txt):
        # code here

        i = 0
        j = 0
        k = len(pat)
        d = dict()
        d2 = dict()

        for p in pat:
            if p not in d2:
                d2[p] = 1
            else:
                d2[p] += 1
        count = 0

        while (j < len(txt)):

            if txt[j] not in d:
                d[txt[j]] = 1
            else:
                d[txt[j]] += 1

            if (j - i + 1) < k:
                j = j + 1
            elif (j - i + 1) == k:
                if d2 == d:
                    count += 1
            d[txt[i]] -= 1

            if d[txt[i]] == 0:
                d.pop(txt[i], None)
            i = i + 1
            j = j + 1

        return count