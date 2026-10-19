class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        i = 0

        if len(strs) == 0:
            return ""
        
        # Shortest word is the max length of prefix

        pre = min(strs, key = len)
        cutoff = len(pre)

        for string in strs:
            print(f"Current String: {string}")
            i = 0
            for char in pre:
                print(f"Current Char: {char}")
                if string[i] == char:
                    i += 1
                else:
                    if cutoff > i:
                        cutoff = i
                    break
        
        print(cutoff)

        return pre[:cutoff]
                