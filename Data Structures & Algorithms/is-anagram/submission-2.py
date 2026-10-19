
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        dic = {}  
    
        for letter in s:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
        
        for letter in t:
            if letter in dic:
                dic[letter] -= 1
            else:
                return False

        return all(count == 0 for count in dic.values())