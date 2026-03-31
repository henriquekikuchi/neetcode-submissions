class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)

        for i in range(len(strs)):
            hs = [0] * 26
            for j in strs[i]:
                idx = ord(j) - 97
                hs[idx] += 1

            hs = str(hs)
            print(hs)

            freq[hs].append(strs[i])

        res = []
        for v in freq.values():
            res.append(v)

        return res