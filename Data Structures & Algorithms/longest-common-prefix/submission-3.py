class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        i = 0

        if len(strs) == 0:
            return ""

        pre = min(strs, key = len)
        cutoff = len(pre)

        for string in strs:
            i = 0
            for char in pre:
                if string[i] == char:
                    i += 1
                else:
                    if cutoff > i:
                        cutoff = i
                    break

        return pre[:cutoff]
                