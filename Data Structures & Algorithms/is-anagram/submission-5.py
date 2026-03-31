class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        two string containing the same characters in any order
        if it is return True, otherwise return false
        """

        if len(s) == 0 and len(t) == 0:
            return True

        if len(s) != len(t):
            return False
        
        freq = [0 for i in range(27)]

        # a is represented as 97 then always subtract it from current char
        # 98 - 97 = 1
        # that given the correct index position

        for i in range(len(s)):
            freq[ord(s[i]) - 97] += 1
            freq[ord(t[i]) - 97] -= 1

        for i in range(len(freq)):
            if freq[i] != 0:
                return False

        return True


