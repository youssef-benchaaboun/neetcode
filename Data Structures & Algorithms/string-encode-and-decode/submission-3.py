class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []

        for s in strs:
            parts.append(str(len(s)) + "#" + s)

        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            str_len = int(s[i:j])
            i = j + 1

            result.append(s[i:i + str_len])
            i += str_len

        return result
