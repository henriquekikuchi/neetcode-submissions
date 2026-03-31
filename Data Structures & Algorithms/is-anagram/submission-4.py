class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        two string containing the same characters in any order
        if it is return True, otherwise return false
        """

        s_freq = [0 for i in range(27)]
        t_freq = [0 for i in range(27)]

        # a is represented as 97 then always subtract it from current char
        # 98 - 97 = 1
        # that given the correct index position
        for c in s:
            s_freq[ord(c) - 97] += 1

        for c in t:
            t_freq[ord(c) - 97] += 1

        return s_freq == t_freq


