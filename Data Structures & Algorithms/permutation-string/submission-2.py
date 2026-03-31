class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = Counter(s1)
        w = Counter(s2[:len(s1)])
        if c == w:
            return True
        for i in range(len(s1),len(s2)):
            w[s2[i]] += 1
            if i >= len(s1):
                w[s2[i-len(s1)]] -= 1
                if w[s2[i-len(s1)]] == 0:
                    del w[s2[i-len(s1)]]         
            if c == w:
                return True

        return False
