class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def check_palindrome(i, j):
            while i < j:
                if not s[i] == s[j]:
                    return False
                i += 1
                j -= 1
            return True

        start = 0
        end = len(s) - 1
        count = 0
        
        while start < end:

            if not s[start] == s[end]:

                ## Test inc of start
                if count >= 1:
                    return False

                return check_palindrome(start + 1, end) or check_palindrome(start, end - 1)

            else:
                start += 1
                end -= 1

        return True