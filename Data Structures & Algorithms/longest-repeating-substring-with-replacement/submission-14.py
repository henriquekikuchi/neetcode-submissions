class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0
        w = Counter()
        count = 0

        maxFreq = 0

        while end < len(s):
            w[s[end]] += 1
            count += 1
            key,value = w.most_common(1)[0]
            if count - w[key] > k:
                count -= 1
                w[s[start]] -= 1
                if w[s[start]] == 0:
                    del w[s[start]]
                start += 1

            maxFreq = max((end-start)+1, maxFreq)
            end += 1
            

        return maxFreq
