class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        l = [0 for i in range(0, num + 1)]

        for i in range(1, num + 1):
            if i % 2 == 0:
                l[i] = l[i >> 1]
            else:
                l[i] = l[i >> 1] + 1

        return l


"""
Here the concept used is if the number is odd , then number of set bits = n/2 +1
Else if the number is even then number of set bits  = n/2 

"""