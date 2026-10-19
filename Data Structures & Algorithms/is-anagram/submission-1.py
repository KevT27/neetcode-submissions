from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        dic_s = defaultdict(int)
        dic_t = defaultdict(int)  
    
        for letter in s:
            dic_s[letter] += 1
        
        for letter in t:
            dic_t[letter] += 1

        return dic_s == dic_t