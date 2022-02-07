class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def count_till_idx(i):
            count = 0
            j = 0
            while (j < i):
                if nums[j] == 0:
                    count = count + 1
                j = j + 1
            return count

        if (target + sum(nums)) % 2 == 0:
            S = (target + sum(nums)) // 2
        else:
            return 0
        if len(nums) == 1 and nums[0] == abs(target):
            return 1
        elif len(nums) == 1 and nums[0] != abs(target):
            return 0

        N = len(nums)
        print("N is", N)

        t = [[0 for i in range(0, S + 1)] for j in range(0, N + 1)]

        for nn in range(0, N + 1):
            t[nn][0] = pow(2, count_till_idx(nn))
        for ss in range(1, S + 1):
            t[0][ss] = 0

        for nn in range(1, N + 1):
            for ss in range(1, S + 1):

                if nums[nn - 1] <= ss:
                    t[nn][ss] = t[nn - 1][ss - nums[nn - 1]] + t[nn - 1][ss]
                else:
                    t[nn][ss] = t[nn - 1][ss]

        return t[N][S]


