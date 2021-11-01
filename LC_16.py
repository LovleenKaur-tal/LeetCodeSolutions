class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = 1001
        lst = sorted(nums)
        res = None
        for i, a in enumerate(lst):
            l = i + 1
            r = len(lst) - 1

            while (l < r):

                s = a + lst[l] + lst[r]

                if abs(target - s) < diff:

                    diff = abs(target - s)
                    res = s
                else:
                    diff = diff

                if s == target:
                    return target
                if s > target:
                    r = r - 1
                else:
                    l = l + 1

        return res




\
