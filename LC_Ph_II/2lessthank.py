class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        x = sorted(nums)

        l = 0
        r = len(nums) - 1
        sm = -1
        mx_sm = -1
        while (l < r):
            sm = x[l] + x[r]
            if sm < k:
                mx_sm = max(mx_sm, sm)
                l = l + 1
            else:
                r = r - 1
        return mx_sm
