class Solution:
    # Back-end complete function Template for Python 3

    # Function to find the leaders in the array.
    def leaders(self, A, N):
        # Code here
        result = []
        result.append(A[len(A) - 1])
        max_from_right = A[len(A) - 1]
        i = len(A) - 2
        while (i >= 0):
            if max_from_right <= A[i]:
                max_from_right = A[i]
                result.append(A[i])
            i = i - 1

        return sorted(result, reverse=True)


"""
Scan from right hand side
"""