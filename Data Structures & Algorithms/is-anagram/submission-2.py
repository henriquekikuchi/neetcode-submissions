class Solution:

    """
    first version:

    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    """     

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cs_frequency = defaultdict(lambda: 0)
        ct_frequency = defaultdict(lambda: 0)

        for c in s:
            cs_frequency[c] += 1
        
        for c in t:
            ct_frequency[c] += 1

        for key, value in cs_frequency.items():
            if ct_frequency[key] != value:
                return False
        
        return True

        

        

