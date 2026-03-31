class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(left: str, right: str):
            freq_left = defaultdict(lambda: 0)
            freq_right = defaultdict(lambda: 0)

            if len(left) != len(right):
                return False

            for c in left:
                freq_left[c] += 1
            for c in right:
                freq_right[c] += 1
            
            for key, value in freq_left.items():
                if freq_right[key] != value:
                    return False
            
            return True

        anagrams = defaultdict(list)
        words_sorteds = set(["".join(sorted(w)) for w in strs])

        for word in strs:
            for word_sorted in words_sorteds:
                if isAnagram(word, word_sorted):
                    anagrams[word_sorted].append(word)
                    break

        return [values for values in anagrams.values()]
