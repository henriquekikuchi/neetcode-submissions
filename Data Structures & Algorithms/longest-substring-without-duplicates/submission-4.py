class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        if len(s) == 2 and s[0] != s[1]: return len(s)

        maxLength = 0

        for i in range(len(s)):
            items = []
            items.append(s[i])
            for j in range(i+1, len(s)):
                if s[j] not in items:
                    items.append(s[j])
                else:
                    break
            maxLength = max(maxLength, len(items))
            items = []

        return maxLength