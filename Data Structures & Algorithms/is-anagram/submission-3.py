class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        two string containing the same characters in any order
        if it is return True, otherwise return false
        """

        return sorted(s) == sorted(t)

