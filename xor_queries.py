class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = []
        i = 0
        pref = []
        for idx, num in enumerate(arr):
            if idx == 0:
                pref.append(num)
            else:
                pref.append(pref[idx - 1] ^ num)

        ans = []
        for lst in queries:
            left = lst[0]
            right = lst[1]
            print("The left and right", left, right)
            if left == 0:
                ans.append(pref[right])
            else:
                ans.append(pref[right] ^ pref[left - 1])
        return ans
