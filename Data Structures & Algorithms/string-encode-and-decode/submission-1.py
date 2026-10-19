class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = []

        for word in strs:
            encoded_string.append(f"{len(word)}/{word}")

        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:

        # Example: 5/apple5/cider
        decoded_strs = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "/":
                j += 1
            
            length = int(s[i:j])
            
            i = j + 1

            decoded_strs.append(s[i : i + length])

            i += length


        return decoded_strs