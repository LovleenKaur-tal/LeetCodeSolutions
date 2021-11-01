class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = dict()
        val = -1
        ans = None
        for i, num in enumerate(nums):
            if num in d.keys():
                val = abs(d[num] - i)
                if val <= k:
                    return True
            d[num] = i
        return False







