class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = defaultdict(lambda: 0)

        for n in nums:
            h[n] += 1

        nums_by_freq = [()] * len(h.keys())
        
        i = 0
        for key, value in h.items():
            nums_by_freq[i] = (key, value)
            i+=1

        nums_by_freq = list(sorted(nums_by_freq, key = lambda x: x[1], reverse=True))
        return list(map(lambda x: x[0], nums_by_freq))[:k]


        return res



        