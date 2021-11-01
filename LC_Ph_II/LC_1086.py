class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """

        d = dict()
        for item in items:
            d[item[0]] = list()

        for item in items:
            d[item[0]].append(item[1])

        l = []
        for k, item in d.items():
            top = sorted(item, reverse=True)[0:5]
            avg_val = sum(top) / len(top)

            l.append([k, avg_val])
        return l


