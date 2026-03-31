class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = re.sub(r'[^A-Za-z0-9 ]', '', s).replace(' ', '').lower()

        length = len(word)
        p1 = 0
        p2 = length - 1
        while p1 < p2:
            if word[p1] == word[p2]:
                p1+=1
                p2-=1
            else:
                return False

        return True