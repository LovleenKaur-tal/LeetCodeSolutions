class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        mn_dist = len(wordsDict)
        pos1, pos2 = -1, -1

        for i, word in enumerate(wordsDict):
            if word == word1:
                pos1 = i
            elif word == word2:
                pos2 = i
            if pos1 != -1 and pos2 != -1:
                mn_dist = min(mn_dist, abs(pos2 - pos1))
        return mn_dist







