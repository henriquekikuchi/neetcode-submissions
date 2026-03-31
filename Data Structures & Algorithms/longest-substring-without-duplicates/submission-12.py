class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)

        maxLen = 0
        l, r, w = 0, 1, Counter()

        w[s[l]] += 1

        while r < len(s):
            w[s[r]] += 1
            while w[s[r]] > 1:
                w[s[l]] -= 1
                if w[s[l]] == 0:
                    del w[s[l]]
                l += 1
            r += 1
            maxLen = max(maxLen, sum(w.values()))

        return maxLen

                