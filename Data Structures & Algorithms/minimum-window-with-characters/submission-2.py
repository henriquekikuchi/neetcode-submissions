class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""
        if len(s) < len(t): return ""

        dq = deque()

        for k, c in enumerate(s):
            if c in t:
                dq.append(k)

        resg = ""

        while dq:
            start = dq.popleft()
            res = ""
            freq = Counter(t)
            for i in range(start, len(s)):
                res += s[i]
                if s[i] in freq.keys():
                    freq[s[i]] -= 1
                    if freq[s[i]] == 0:
                        del freq[s[i]]
                if not freq:
                    if len(res) < len(resg) or not resg:
                        resg = res
        return resg




            


