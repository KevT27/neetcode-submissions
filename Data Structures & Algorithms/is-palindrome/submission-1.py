class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        r = len(s) - 1

        while i < r:

            while not s[i].isalnum() and i < r:
                i += 1
            start = s[i].lower()

            while not s[r].isalnum() and i < r:
                r -= 1
            end = s[r].lower()

            if start.lower() != end.lower():
                return False

            i += 1
            r -= 1

        return True