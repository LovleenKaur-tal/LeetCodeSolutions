class Solution(object):
    def twoSumLessThanK(self, nums, k):

        nums = sorted(nums)
        n = len(nums)
        l, r = 0, (n - 1)
        out = -1
        while (l < r and r < n):
            summ = nums[l] + nums[r]
            if summ >= k:
                r = r - 1
            else:
                out = max(out, summ)
                l = l + 1
        return out

# 2 ptr approach