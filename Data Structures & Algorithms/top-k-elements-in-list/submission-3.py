class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = defaultdict(lambda: [])
        res = []

        for key, value in counter.items():
            freq[value].append(key)
        
        freqKeysSorted = sorted(freq.keys(), reverse=True)

        for key in freqKeysSorted:
            res += freq[key]
            if len(res) >= k:
                break 

        return res

