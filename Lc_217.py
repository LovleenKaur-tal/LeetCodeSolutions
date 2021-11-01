class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_lst = sorted(nums)

        for i in range(1, len(new_lst)):
            prev = new_lst[i - 1]
            curr = new_lst[i]
            if curr ^ prev == 0:
                return True
        return False

