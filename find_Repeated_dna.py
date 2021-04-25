class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashmap = {}
        result = []

        for i in range(0, len(s)):
            substr = s[i:i + 10]
            if substr in hashmap:
                hashmap[substr] += 1
            else:
                hashmap[substr] = 1

            if hashmap[substr] > 1 and substr not in result:
                result.append(substr)
        return result



""""
hashing!
"""