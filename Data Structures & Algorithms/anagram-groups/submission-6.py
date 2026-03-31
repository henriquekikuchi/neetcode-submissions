class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)

        for i in range(len(strs)):
            hs = str(sorted(strs[i]))
            freq[hs].append(strs[i])

        res = []
        for v in freq.values():
            res.append(v)

        return res