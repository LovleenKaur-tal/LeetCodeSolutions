from collections import Counter

"350. Intersection of Two Arrays II"

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        return list((Counter(nums1) & Counter(nums2)).elements())


'''Comments
1. Counter used to create a hashmap and it keeps "key" as "varibal" and "value" as count
2. We can apply all set operations in Counter.

'''
