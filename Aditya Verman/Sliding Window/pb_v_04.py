class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l = 0
        r = 0

        min_range = [-1, -1]
        min_len = float("inf")
        d = dict()
        for val in t:
            if val not in d:
                d[val] = 1

            else:
                d[val] = d[val] + 1
        count = len(d.keys())

        need = count
        have = 0
        window = dict()
        while (r < len(s)):

            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in d and window[s[r]] == d[s[r]]:
                have = have + 1

            while have == need:
                if r - l + 1 < min_len:
                    min_range = [l, r]
                    min_len = r - l + 1

                window[s[l]] -= 1

                if s[l] in d and window[s[l]] < d[s[l]]:
                    have = have - 1
                l = l + 1
            r = r + 1
        l, r = min_range

        return s[l:r + 1] if min_len != float("inf") else ""

