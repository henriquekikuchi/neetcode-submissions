class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)

        if k > n:
            return False

        s = 0
        e = k
        w = s2[:e]
        o_s1 = sorted(s1)

        while e <= n:
            if o_s1 == sorted(w):
                return True

            s+=1
            e+=1
            w = s2[s:e]

        return False
