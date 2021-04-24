class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 0
        if n < 0:
            return False
        for i in range(0, 32):
            if (n >> i) & 1:
                count = count + 1

        if count == 1:
            return True
        else:
            return False


"""
1. We can either count number of bits.

2. Or direct approach is given below:

"""