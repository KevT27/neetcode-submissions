class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        word = ""
        last_ind = 0
        temp = min(word1, word2, key=len)

        for i, l in enumerate(temp):
            if temp == word1:
                word += l
                word += word2[i]
            else:
                word += word1[i]
                word += l

            last_ind = i
        
        if len(word2) > len(word1):
            word += word2[last_ind + 1:]
        elif len(word2) < len(word1):
            word += word1[last_ind + 1:]

        return word